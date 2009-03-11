from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^jlcaro/', include('jlcaro.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/(.*)',admin.site.root),
    
    url(r'^$', 'django.views.generic.simple.direct_to_template',{'template':'home.html'}),
    url(r'^contact/?$','django.views.generic.simple.direct_to_template',{'template':'contact.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns ('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
    )
