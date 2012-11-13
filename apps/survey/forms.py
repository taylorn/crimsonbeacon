from apps.survey.models import Survey
from django.forms import ModelForm, TextInput, Textarea, MultipleChoiceField


class SurveyCreateForm(ModelForm):
    
    class Meta:
        model = Survey
        fields = ('title', 'subtitle', 'link', 'body', 'link_display_method')
        widgets = {
           'title': TextInput(attrs={'size': 87, 'autofocus': True}),
           'subtitle': TextInput(attrs={'size': 87}),
           'link': TextInput(attrs={'size': 87}),
           'body': Textarea(attrs={'rows': 10, 'cols': 116})
        }
        
class SurveyUpdateForm(SurveyCreateForm):
    pass