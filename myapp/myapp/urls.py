import os
import django

from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^myapp/', include('myapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#	url(r'^$','iopapp.views.login', name='LOGIN_URL'),
#	url(r'^$', 'iopapp.views.menu'),
	url(r'^iopapp/', include('iopapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
