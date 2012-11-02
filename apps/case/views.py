from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from apps.case.models import Case

class CaseDetailView(DetailView):
    
    model = Case
    
class CaseListView(ListView):
    pass

class CaseCreateView(CreateView):
    pass