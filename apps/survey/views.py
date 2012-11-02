from apps.survey.forms import SurveyCreateForm
from apps.survey.models import Survey
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

class SurveyDetailView(DetailView):
    
    template_name_suffix = '_detail.html'
    model = Survey
    
    def get_context_data(self, **kwargs):
        context = super(SurveyDetailView, self).get_context_data(**kwargs)
        return context
    
#    def get_queryset(self):
#        results = super(SurveyDetailView, self).get_queryset()
#        print results, '==queryset'
#        return results
#    
    def get_object(self):
        survey = self.get_queryset().get(title=self.kwargs['title'])
        return survey
        
class SurveyListView(ListView):
    
    template_name = 'survey/templates/survey_list.html'
    model = Survey
    
    def get_context_data(self, **kwargs):
        context = super(SurveyListView, self).get_context_data(**kwargs)
        context['sidebar_on']=False
        return context
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(SurveyListView, self).get_queryset(*args, **kwargs)
        return queryset

class SurveyCreateView(CreateView):
    
    form_class = SurveyCreateForm
    model = Survey
    template_name = 'survey/templates/survey_create.html'
    success_url = reverse_lazy('survey_list')
    
    def dispatch(self, *args, **kwargs):
        return super(SurveyCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        print 'Survey has been created'
        return super(SurveyCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        print 'Form is invalid'
        return super(SurveyCreateView, self).form_valid(form)
    