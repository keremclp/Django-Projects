from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',unique=True)
    isActive = models.BooleanField(default=False)

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            "category_view", 
            kwargs={"category_slug": self.slug}
        )



class ToDo(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True) 
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "todo_detail_view", 
            kwargs={
                "category_slug": self.category.slug,
                "id": self.pk
            }
        )