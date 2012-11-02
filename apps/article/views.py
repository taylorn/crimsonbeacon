from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from apps.article.models import Article

class ArticleListView(ListView):
    
    template_name = 'article/article_list.html'
    
class ArticleCreateView(CreateView):
    
    model = Article

class ArticleDetailView(DetailView):
    
    model = Article
