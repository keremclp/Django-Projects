from django.contrib import admin
from .models import Todo, TodoTag,TodoCategory
# Register your models here.
class TodoCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'isActive',
    
    ]

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'category',
        'title',
        'isActive',
        
        # 'created_at',
        # 'updated_at', 
    ]
    list_display_links = [
        'id',
        'title',
        'category',
    ]

admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoCategory,TodoCategoryAdmin)
admin.site.register(TodoTag)
