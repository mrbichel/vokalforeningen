from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap
from django.views.generic.simple import redirect_to, direct_to_template
from django.conf import settings

admin.autodiscover()

sitemaps = {
    'pages': FlatPageSitemap,
}



urlpatterns = patterns('',

    url(r'^login/$', 'profiles.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'profiles/logged_out.html', 'next_page': '/'}, name="logout"),

    url(r'^registration/$', 'profiles.views.registration', name="registration"),

    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^notification/', include('notification.urls')),
    
    url(r'^$', 'views.index', name='index'),
    url(r'^a/doc/', include('django.contrib.admindocs.urls')),
    url(r'^a/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),

    url(r'^o/', include('corkboard.urls')),
    url(r'^p/', include('profiles.urls')),
    url(r'^m/', include('meetings.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$',
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)