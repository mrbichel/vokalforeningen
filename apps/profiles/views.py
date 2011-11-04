# coding=utf-8

import pprint
from django.core.mail import mail_managers, send_mail
from django.db.models.aggregates import Count
from profiles.models import Profile
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.generic import list_detail, date_based
from django.contrib.auth import authenticate, login
from django.template import loader, Context

from forms import ProfileForm, UserForm
import settings

from profiles.forms import RegistrationForm

PAGINATE_MEMBERS_BY = getattr(settings, 'PAGINATE_BY', 30)

def list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Profile.objects.filter(user__is_active=True),
        paginate_by=PAGINATE_MEMBERS_BY,
        **kwargs
    )

def detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "profiles/profile_detail.html", {'profile': user.get_profile()})


def update(request, id):
    user = get_object_or_404(User, id=id)
    profile = user.get_profile()

    if request.user == user:
        if request.method == 'POST':
            pform = ProfileForm(request.POST, instance=profile)
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

def registration(request):
    if request.user.is_authenticated():
         # They already have an account; don't let them register again
        return render(request, 'profiles/registration.html', {'has_account': True})

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #pprint.pprint(form.cleaned_data)
            data = form.cleaned_data
            user = User(username=data['email'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'])
            user.set_password(data['password1'])
            user.is_active = False
            user.save()

            profile = user.get_profile()

            profile.address = data['address']
            profile.postal_code = data['postal_code']
            profile.city = data['city']
            profile.mobile_phone_number = data['mobile_phone_number']

            profile.save()

            mail_managers('DVF: Nyt medlem.', '{} vil gerne være medlem i Dansk Vokalforening. Husk at aktivere personens bruger når kontingent er gået ind på kontoen.'.format(user.get_full_name) , settings.DEFAULT_FROM_EMAIL)

            t = loader.get_template('profiles/registration_email.txt')
            c = Context({
                'name': user.get_full_name(),
            })
            send_mail('Indmeldelse i Dansk Vokalforening', t.render(c), settings.DEFAULT_FROM_EMAIL, [user.email])

            return render(request, "profiles/registration_complete.html")
    else:
        form = RegistrationForm()


    return render(request, "profiles/registration.html", {'form': form})