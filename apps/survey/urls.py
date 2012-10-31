from apps.survey.views import SurveyDetailView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       
    url(r'^(?P<urltag>[a-z0-9_-]{3,33})$', SurveyDetailView.as_view(), name='survey_detail')
    
)