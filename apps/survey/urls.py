from apps.survey.views import SurveyListView, SurveyDetailView, SurveyCreateView, \
    SurveyUpdateView, SurveyDeleteView
from django.conf.urls import patterns, url

urlpatterns = patterns('',   
    url(r'^create/$', SurveyCreateView.as_view(), name='survey_create'),     
    url(r'^$', SurveyListView.as_view(), name='survey_list'),        
    url(r'^(?P<title>[a-z0-9_-]{1,50})$', SurveyDetailView.as_view(), name='survey_detail'),
    url(r'^(?P<title>[a-z0-9_-]{1,50})/update/$', SurveyUpdateView.as_view(), name='survey_update'),
    url(r'^(?P<title>[a-z0-9_-]{1,50})/delete/$', SurveyDeleteView.as_view(), name='survey_delete'),
)




