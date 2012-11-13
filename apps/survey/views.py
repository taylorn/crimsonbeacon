from apps.survey.forms import SurveyCreateForm,SurveyUpdateForm
from apps.survey.models import Survey
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

class SurveyDetailView(DetailView):
    
    template_name = 'survey/templates/survey_detail.html'
    model = Survey
    
    def get_context_data(self, **kwargs):
        context = super(SurveyDetailView, self).get_context_data(**kwargs)
        return context
    
    def get_object(self):
        survey = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return survey
        
class SurveyListView(ListView):
    
    template_name = 'survey/templates/survey_list.html'
    model = Survey
    
    def get_context_data(self, **kwargs):
        context = super(SurveyListView, self).get_context_data(**kwargs)
        context['sidebar_on']=True
        return context

class SurveyCreateView(CreateView):
    
    form_class = SurveyCreateForm
    template_name = 'survey/templates/survey_create.html'
    success_url = reverse_lazy('survey_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(SurveyCreateView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('survey_list'))
    
class SurveyUpdateView(UpdateView):
    
    form_class = SurveyUpdateForm
    model = Survey
    template_name = 'survey/templates/survey_update.html'
    success_url = reverse_lazy('survey_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(SurveyCreateView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('survey_list'))
    
    def get_object(self):
        survey = self.get_queryset().get(title=self.kwargs['title'])
        return survey
    
    