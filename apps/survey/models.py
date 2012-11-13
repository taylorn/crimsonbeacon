from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Survey(models.Model):
    
    title = models.CharField(max_length=50)
    subtitle = models.TextField(blank=True)
    body = models.TextField(blank=True)
    
    def get_absolute_url(self):
        return reverse('survey_detail', kwargs={'title': self.title.replace(' ', '-') })