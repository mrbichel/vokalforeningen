from __future__ import unicode_literals
from django.conf.urls import patterns, url
from views import Memberlist, Grouplist


urlpatterns = patterns('profiles.views',
    url(r'^$',
        Memberlist.as_view(),
        name='profiles_index'
    ),

    url(r'^group/(?P<id>\d+)/$',
        Grouplist.as_view(),
        name='profiles_group'
    ),

    url(r'^(?P<id>\d+)/$',
        'detail',
        name='profile_detail'
    ),

    url(r'^(?P<id>\d+)/update/$',
        'update',
        name='profile_update'
    ),


)
