from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns('corkboard.views',
    url(r'^(?P<id>\d+)/$',
        'detail',
        name='note_detail'
    ),

    url(r'^e$',
        'event_list',
        name='corkboard_events',
    ),

    url(r'^n$',
        'note_list',
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
        'by_category',
        name='note_by_category'
    ),

)
