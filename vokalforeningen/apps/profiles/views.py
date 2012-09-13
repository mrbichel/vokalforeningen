# coding=utf-8
from __future__ import unicode_literals
import uuid
from django.core.mail import mail_managers, send_mail
from profiles.models import Profile
from django.contrib.auth.views import login as login_view
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.generic import list_detail
from django.template import loader, Context
from profiles.forms import LoginForm

from forms import ProfileForm, UserForm
from django.conf import settings

from profiles.forms import RegistrationForm

PAGINATE_MEMBERS_BY = getattr(settings, 'PAGINATE_BY', 30)

def group(request, id, **kwargs):

    groups = Group.objects.all()
    group = get_object_or_404(Group, id=id)

    return list_detail.object_list(
        request,
        queryset=Profile.objects.filter(user__groups=group),
        template_name="profiles/profile_group.html",
        extra_context={"groups": groups, "group": group,},
        **kwargs
    )

def list(request, **kwargs):

    groups = Group.objects.all()

    return list_detail.object_list(
        request,
        queryset=Profile.objects.filter(user__is_active=True).order_by('user__first_name'),
        extra_context={"groups": groups},
        paginate_by=PAGINATE_MEMBERS_BY,
        **kwargs
    )

def detail(request, id):

    groups = Group.objects.all()


    user = get_object_or_404(User, id=id)
    return render(request, "profiles/profile_detail.html", {'profile': user.get_profile(), 'groups': groups,})
 
def update(request, id):
    user = get_object_or_404(User, id=id)
    profile = user.get_profile()

    if request.user == user:
        if request.method == 'POST':
            pform = ProfileForm(request.POST, request.FILES, instance=profile)
            uform = UserForm(request.POST, instance=user)

            if pform.is_valid() and uform.is_valid():
                pform.save()
                uform.save()

                return HttpResponseRedirect(profile.get_absolute_url())
        else:
            pform = ProfileForm(instance=profile)
            uform = UserForm(instance=user)

        return render(request, "profiles/profile_form.html", {'pform': pform, 'uform': uform})
    else:
        return HttpResponseForbidden("Du har ikke tilladelse til at redigere denne profile.")

def login(request):
    return login_view(request, template_name='profiles/login.html', authentication_form=LoginForm)

def registration(request):
    if request.user.is_authenticated():
         # They already have an account; don't let them register again
        return render(request, 'profiles/registration.html', {'has_account': True})

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #pprint.pprint(form.cleaned_data)
            data = form.cleaned_data
            user = User(first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'])

            username = uuid.uuid4().hex[:30]
            try:
                while True:
                    User.objects.get(username=username)
                    username = uuid.uuid4().hex[:30]
            except User.DoesNotExist:
                pass

            user.username = username

            user.set_password(data['password1'])
            user.is_active = False
            user.save()

            profile = user.get_profile()

            profile.address = data['address']
            profile.postal_code = data['postal_code']
            profile.city = data['city']
            profile.mobile_phone_number = data['mobile_phone_number']

            profile.save()

            t = loader.get_template('profiles/registration_email.txt')
            c = Context({
                'name': user.get_full_name(),
            })
            send_mail('Indmeldelse i Dansk Vokalforening', t.render(c), settings.DEFAULT_FROM_EMAIL, [user.email])
            
            mail_managers('DVF: Nyt medlem.', '{} vil gerne være medlem i Dansk Vokalforening. Husk at aktivere personens bruger når kontingent er gået ind på kontoen.'.format(user.get_full_name()) , settings.DEFAULT_FROM_EMAIL)
            

            return render(request, "profiles/registration_complete.html")
    else:
        form = RegistrationForm()


    return render(request, "profiles/registration.html", {'form': form})


#def emailInactive(request):
