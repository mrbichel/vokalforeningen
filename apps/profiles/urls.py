from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^$',
        'list',
        name='profiles_index'
    ),

    url(r'^(?P<username>[-\w]+)/$',
        'detail',
        name='profile_detail'
    ),



)
