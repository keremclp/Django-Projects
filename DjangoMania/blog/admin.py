from django.contrib import admin
from blog.models import BlogCategory,BlogTag,Post

# Register your models here.
@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'isActive',
        'view_count',
    ]
