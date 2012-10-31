from django.db import models

# Create your models here.

class Survey(models.Model):
    
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, null=True)
    body = models.TextField(blank=True)