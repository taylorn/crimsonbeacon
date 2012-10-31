from django.db import models

# Create your models here.

class Survey(models.Model):
    
    title = models.CharField(max_length=33)
    body = models.TextField(blank=True)