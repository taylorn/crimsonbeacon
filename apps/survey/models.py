from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Survey(models.Model):
    
    LINK_DISPLAY_METHODS = (
        ('embedded', 'Embedded (within page)'), 
        ('external', 'External (linked to another site)'),
        ('internal', 'Internal (linked to detail page on this site)')
    )
    
    title = models.CharField(max_length=50)
    subtitle = models.TextField(blank=True)
    body = models.TextField(blank=True)
    link = models.URLField(blank=True)
    link_display_method = models.CharField(max_length=8, 
                                           choices=LINK_DISPLAY_METHODS,
                                           default='embedded')
    
    def get_absolute_url(self):
        return reverse('survey_detail', kwargs={'title': self.title.replace(' ', '-') })
    
    def get_referenced_page(self):
        if self.link_display_method in ('embedded', 'external'):
            return self.link
        elif self.link_display_method == 'internal':
            return self.get_absolute_url()
    
    def get_update_url(self):
        return reverse('survey_update', kwargs={'title': self.title.replace(' ', '-') })
    
    def get_delete_url(self):
        return reverse('survey_delete', kwargs={'title': self.title.replace(' ', '-') })
    
    def has_embedded_link(self):
        return self.link_display_method == 'embedded'
        