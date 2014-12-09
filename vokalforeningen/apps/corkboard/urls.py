from __future__ import unicode_literals
from django.conf.urls import patterns, url
from views import EventList, ByCategory, NoteList

urlpatterns = patterns('corkboard.views',
    url(r'^(?P<id>\d+)/$',
        'detail',
        name='note_detail'
    ),

    url(r'^e$',
        EventList.as_view(),
        name='corkboard_events',
    ),

    url(r'^n$',
        NoteList.as_view(),
        name='corkboard_notes'
    ),

    url(r'^create$',
        'create', {'event': False},
        name='note_create'
    ),

    url(r'^create/event$',
        'create', {'event': True},
        name='event_create'
    ),

    url(r'^(?P<id>\d+)/update/$',
        'update',
        name='note_update'
    ),

    url(r'^(?P<id>\d+)/delete/$',
        'delete',
        name='note_delete'
    ),

    url(r'^(?P<slug>[^/]+)/$',
        ByCategory.as_view(),
        name='note_by_category'
    ),

)
