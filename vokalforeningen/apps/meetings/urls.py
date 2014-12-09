from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('meetings.views',
    url(r'^(?P<id>\d+)/$',
        'detail',
        name='meeting_detail'
    ),
    url(r'^$',
        'list',
        name='meetings_index'
    ),
)
