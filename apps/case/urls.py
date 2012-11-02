from apps.case.views import CaseListView, CaseDetailView, CaseCreateView
from django.conf.urls import patterns, url

urlpatterns = patterns('',                
#    url(r'^(?P<urltag>[a-z0-9_-]{3,33})$', CaseDetailView.as_view(name=urltag), name='case_detail')
    url(r'^$', CaseListView.as_view(), name='case_list'),
    url(r'^create$', CaseCreateView.as_view(), name='case_create'),
)