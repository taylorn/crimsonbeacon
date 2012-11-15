from crimsonbeacon import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
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
                       
    url(r'^$', 'crimsonbeacon.views.index', name='index'),
    url(r'^articles/', include('apps.article.urls')),
    url(r'^survey-reports/', include('apps.survey.urls')),
    url(r'^case-studies/', include('apps.case.urls')),
    url(r'^%s/$' % settings.ADMIN_PANEL_URL, 'crimsonbeacon.views.admin_panel_view'),
    url(r'^admin-login/$', 'crimsonbeacon.views.login_view', name='admin_login'),

)

urlpatterns += patterns('django.contrib.flatpages.views',
    
    
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^contributor/$', 'flatpage', {'url': '/contributor/'}, name='contributor'),
    url(r'^contact/$', 'flatpage', {'url': '/contact/'}, name='contact'),
)

urlpatterns += staticfiles_urlpatterns()