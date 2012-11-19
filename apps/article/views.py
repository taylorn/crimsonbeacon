from apps.article.forms import ArticleCreateForm, ArticleUpdateForm
from apps.article.models import Article
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

class ArticleDetailView(DetailView):
    
    template_name = 'article/templates/article_detail.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context
    
    def get_object(self):
        article = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return article
        
class ArticleListView(ListView):
    
    template_name = 'article/templates/article_list.html'
    model = Article
            
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['sidebar_on']=True
        if self.request.user.is_staff:
            context['user_is_staff'] = True
        return context

class ArticleCreateView(CreateView):
    
    form_class = ArticleCreateForm
    template_name = 'article/templates/article_create.html'
    success_url = reverse_lazy('article_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(ArticleCreateView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('article_list'))
    
class ArticleUpdateView(UpdateView):
    
    form_class = ArticleUpdateForm
    model = Article
    template_name = 'article/templates/article_update.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('article_detail', kwargs={'title': kwargs['title']}))
    
    def get_object(self):
        article = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return article
    
class ArticleDeleteView(DeleteView):
    
    model = Article
    template_name = 'article/templates/article_delete.html'
    success_url = reverse_lazy('article_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(ArticleDeleteView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('article_list'))
    
    def get_object(self):
        article = self.get_queryset().get(title=self.kwargs['title'].replace('-', ' '))
        return article
        
    
    