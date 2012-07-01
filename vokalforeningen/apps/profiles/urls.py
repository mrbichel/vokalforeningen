from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$',
        'list',
        name='profiles_index'
    ),

    url(r'^board/$',
        'board',
        name='profiles_board'
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
