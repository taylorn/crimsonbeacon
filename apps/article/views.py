# Create your views here.
from django.views.generic.list import ListView

class ArticleListView(ListView):
    
    template_name = 'article/article_list.html'

