from apps.case.views import CaseListView, CaseDetailView, CaseCreateView, \
    CaseUpdateView, CaseDeleteView
from django.conf.urls import patterns, url

urlpatterns = patterns('',   
    url(r'^create/$', CaseCreateView.as_view(), name='case_create'),     
    url(r'^$', CaseListView.as_view(), name='case_list'),        
    url(r'^(?P<title>[a-z0-9_-]{1,50})$', CaseDetailView.as_view(), name='case_detail'),
    url(r'^(?P<title>[a-z0-9_-]{1,50})/update/$', CaseUpdateView.as_view(), name='case_update'),
    url(r'^(?P<title>[a-z0-9_-]{1,50})/delete/$', CaseDeleteView.as_view(), name='case_delete'),
)




