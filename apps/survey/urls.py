from apps.survey.views import SurveyListView, SurveyDetailView, SurveyCreateView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',                
#    url(r'^(?P<urltag>[a-z0-9_-]{3,33})$', SurveyDetailView.as_view(name=urltag), name='survey_detail')
    url(r'^$', SurveyListView.as_view(), name='survey_list'),
    url(r'^create$', SurveyCreateView.as_view(), name='survey_create'),
)