from apps.case.forms import CaseCreateForm, CaseUpdateForm
from apps.case.models import Case
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

class CaseDetailView(DetailView):
    
    template_name = 'case/templates/case_detail.html'
    model = Case
    
    def get_context_data(self, **kwargs):
        context = super(CaseDetailView, self).get_context_data(**kwargs)
        return context
    
    def get_object(self):
        case = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return case
        
class CaseListView(ListView):
    
    template_name = 'case/templates/case_list.html'
    model = Case
            
    def get_context_data(self, **kwargs):
        context = super(CaseListView, self).get_context_data(**kwargs)
        context['sidebar_on']=True
        if self.request.user.is_staff:
            context['user_is_staff'] = True
        return context

class CaseCreateView(CreateView):
    
    form_class = CaseCreateForm
    template_name = 'case/templates/case_create.html'
    success_url = reverse_lazy('case_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(CaseCreateView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('case_list'))
    
class CaseUpdateView(UpdateView):
    
    form_class = CaseUpdateForm
    model = Case
    template_name = 'case/templates/case_update.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(CaseUpdateView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('case_detail', kwargs={'title': kwargs['title']}))
    
    def get_object(self):
        case = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return case
    
class CaseDeleteView(DeleteView):
    
    model = Case
    template_name = 'case/templates/case_delete.html'
    success_url = reverse_lazy('case_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(CaseDeleteView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('case_list'))
    
    def get_object(self):
        case = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return case
        
    
    