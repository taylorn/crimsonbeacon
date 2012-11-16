from apps.article.models import Article
from django.forms import ModelForm, TextInput, Textarea, MultipleChoiceField


class ArticleCreateForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ('title', 'subtitle', 'link', 'body', 'link_display_method')
        widgets = {
           'title': TextInput(attrs={'size': 87, 'autofocus': True}),
           'subtitle': TextInput(attrs={'size': 87}),
           'link': TextInput(attrs={'size': 87}),
           'body': Textarea(attrs={'rows': 10, 'cols': 116})
        }
        
class ArticleUpdateForm(ArticleCreateForm):
    pass