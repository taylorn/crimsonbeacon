from apps.article.views import ArticleListView, ArticleDetailView, ArticleCreateView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',                
#    url(r'^(?P<urltag>[a-z0-9_-]{3,33})$', DetailView.as_view(name=urltag), name='_detail')
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^create$', ArticleCreateView.as_view(), name='article_create'),
)