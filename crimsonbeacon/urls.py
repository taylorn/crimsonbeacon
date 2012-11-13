from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from crimsonbeacon import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crimsonbeacon.views.home', name='home'),
    # url(r'^crimsonbeacon/', include('crimsonbeacon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),         

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
                       
    url(r'^articles/', include('apps.article.urls')),
    url(r'^survey-reports/', include('apps.survey.urls')),
    url(r'^case-studies/', include('apps.case.urls')),

)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^contributor/$', 'flatpage', {'url': '/about/'}, name='contributor'),
    url(r'^contact/$', 'flatpage', {'url': '/about/'}, name='contact'),
)

urlpatterns += staticfiles_urlpatterns()