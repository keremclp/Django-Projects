from django.contrib import admin
from blog.models import Category, Tag, BlogPost,UserPostFav
# Register your models here.

@admin.register(UserPostFav)
class UserPostFavAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'pk',
        'user',
        'post',
        'is_deleted',
    )

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

