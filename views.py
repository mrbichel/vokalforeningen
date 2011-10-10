# -*- coding: utf-8 -*-

from django.shortcuts import render
from corkboard.models import Note, Category
from profiles.models import Profile
from django.contrib.auth.models import User
from meetings.models import Meeting


def index(request):

    notes = Note.objects.all()
    meetings = Meeting.objects.all()
    members = Profile.objects.all()

    return render(request, "index.html", {'notes': notes,
                                          'meetings': meetings,
                                          'members': members})

def dashboard(request):
    return render(request, "dashboard.html")

def pages(request):
    pages = []
    return render(request, "pages.html", {'pages': pages})
