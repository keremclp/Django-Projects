from django.contrib import admin
from blog.models import Category, Tag, BlogPost
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'title',
        'isActive',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'isActive',
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'isActive',
        'view_count',
    )
