#!/usr/bin/env python

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # access "liquor_locator" application and indicate liquor_locator application urls to be imported
    url(r'^', include('liquor_locator.urls')), # ADD THIS NEW TUPLE!

    url(r"^ratings/", include("pinax.ratings.urls")),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )