from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('corkboard.views',
    url(r'^(?P<id>\d+)/$',
        'detail',
        name='note_detail'
    ),

    url(r'^$',
        'list',
        name='corkboard_index'
    ),

    url(r'^create$',
        'create',
        name='note_create'
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
