from apps.survey.views import SurveyListView, SurveyDetailView, SurveyCreateView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',   
    url(r'^create$', SurveyCreateView.as_view(), name='survey_create'),     
    url(r'^$', SurveyListView.as_view(), name='survey_list'),        
    url(r'^(?P<title>[a-z0-9_-]{1,50})$', SurveyDetailView.as_view(), name='survey_detail'),
)