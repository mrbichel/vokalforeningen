# -*- coding: utf-8 -*-

from django.shortcuts import render
from corkboard.models import Note, Category
from profiles.models import Profile
from django.contrib.auth.models import User
from meetings.models import Meeting


def index(request):

    notes = Note.objects.all()[:4]
    meetings = Meeting.objects.all()[:4]
    members = Profile.objects.filter(user__is_active=True)[:16]

    return render(request, "index.html", {'notes': notes,
                                          'meetings': meetings,
                                          'members': members})

def dashboard(request):
    return render(request, "dashboard.html")

def pages(request):
    return render(request, "pages.html")
