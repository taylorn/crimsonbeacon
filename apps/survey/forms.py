from django.forms import ModelForm, TextInput, Textarea
from apps.survey.models import Survey


class SurveyCreateForm(ModelForm):
    
    class Meta:
        model = Survey
        fields = ('title', 'subtitle', 'body')
        widgets = {
           'title': TextInput(attrs={'size': 87, 'autofocus': True}),
           'subtitle': TextInput(attrs={'size': 87}),
           'body': Textarea(attrs={'rows': 10, 'cols': 116})
        }
        
class SurveyUpdateForm(ModelForm):
    
    class Meta:
        model = Survey
        fields = ('title', 'subtitle', 'body')
        widgets = {
           'title': TextInput(attrs={'size': 65, 'autofocus': True}),
           'subtitle': TextInput(attrs={'size': 65}),
           'body': Textarea(attrs={'rows': 10, 'cols': 88})
        }