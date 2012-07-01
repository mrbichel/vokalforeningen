# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from corkboard.models import Note, Category
from profiles.models import Profile
from meetings.models import Meeting

def index(request):
    
    notes = Note.objects.filter(is_event=False).order_by('-pub_date')[:3]
    events = Note.objects.filter(is_event=True, end__gte=datetime.datetime.now()-datetime.timedelta(days=1)).order_by('start')[:3]
    
    meetings = Meeting.objects.all()[:4]
    members = Profile.objects.filter(user__is_active=True)[:16]
    
    return render(request, "index.html", {'notes': notes,
                                          'events': events,
                                          'meetings': meetings,
                                          'members': members})
