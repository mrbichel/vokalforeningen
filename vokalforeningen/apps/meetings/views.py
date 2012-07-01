import datetime

from django.db.models.aggregates import Count
from meetings.models import Meeting
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import list_detail, date_based
import settings

PAGINATE_BY = getattr(settings, 'PAGINATE_BY', 12)

def list(request, **kwargs):
    
    meetings = Meeting.objects.all()
    
    future = meetings.filter(date__gte=datetime.datetime.now()-datetime.timedelta(days=1)).order_by("-date")
    past = meetings.exclude(date__gte=datetime.datetime.now()-datetime.timedelta(days=1)).order_by("-date")
    
    return render(request, "meetings/meeting_list.html", {'future_meetings': future, 'past_meetings': past})
    

def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, "meetings/meeting_detail.html", {'object': meeting})