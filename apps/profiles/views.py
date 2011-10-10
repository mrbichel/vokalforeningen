import pprint
from django.db.models.aggregates import Count
from profiles.models import Profile
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import list_detail, date_based
from django.contrib.auth import authenticate, login
import settings

from profiles.forms import RegistrationForm

PAGINATE_MEMBERS_BY = getattr(settings, 'PAGINATE_BY', 30)

def list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Profile.objects.all(),
        paginate_by=PAGINATE_MEMBERS_BY,
        **kwargs
    )

def detail(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.get_profile()

    return render(request, "profiles/profile_detail.html", {'profile': profile})


def registration(request):
    if request.user.is_authenticated():
         # They already have an account; don't let them register again
        return render(request, 'profiles/register.html', {'has_account': True})

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #pprint.pprint(form.cleaned_data)
            data = form.cleaned_data
            user = User(username=data['username'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'])
            user.set_password(data['password1'])
            user.active = False
            user.save()

            profile = user.get_profile()

            profile.address = data['address']

            profile.save()

            return render(request, "profiles/registration_complete.html")
    else:
        form = RegistrationForm()


    return render(request, "profiles/registration.html", {'form': form})