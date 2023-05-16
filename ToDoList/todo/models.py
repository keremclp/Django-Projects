from django.db import models

# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True) 
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)