from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$',
        'list',
        name='profiles_index'
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
