from apps.article.views import ArticleListView, ArticleDetailView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView
from django.conf.urls import patterns, url

urlpatterns = patterns('',   
    url(r'^create/$', ArticleCreateView.as_view(), name='article_create'),     
    url(r'^$', ArticleListView.as_view(), name='article_list'),        
    url(r'^(?P<title>[a-z0-9_-]{1,50})$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^(?P<title>[a-z0-9_-]{1,50})/update/$', ArticleUpdateView.as_view(), name='article_update'),
    url(r'^(?P<title>[a-z0-9_-]{1,50})/delete/$', ArticleDeleteView.as_view(), name='article_delete'),
)




