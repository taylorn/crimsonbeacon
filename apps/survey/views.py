from apps.survey.models import Survey
from django.views.generic.detail import DetailView

class SurveyDetailView(DetailView):
    
    template_name_suffix = '_detail.html'
    model = Survey
    
    def get_context_data(self, **kwargs):
        context = super(SurveyDetailView, self).get_context_data(**kwargs)
        print context, '--context'
        return context
    
    def get_queryset(self):
        results = super(SurveyDetailView, self).get_queryset()
        print results, '==queryset'
        return results
    
    def get_object(self):
        survey = super(SurveyDetailView, self).get_object()
        print survey, '--survey'
        return survey
        