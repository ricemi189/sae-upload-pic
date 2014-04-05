from django.conf.urls.defaults import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vp104dpIc.uploadpic.views.home', name='home'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':os.path.dirname(os.path.realpath(__file__))+'/static/'}),
    # url(r'^vp104dpIc/', include('vp104dpIc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
