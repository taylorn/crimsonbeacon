from django.conf.urls import patterns, include, url
from crimsonbeacon import settings
from apps.article.views import ArticleListView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crimsonbeacon.views.home', name='home'),
    # url(r'^crimsonbeacon/', include('crimsonbeacon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),         

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
                       
    url(r'^articles/$', ArticleListView.as_view(), name='article_list'),
)