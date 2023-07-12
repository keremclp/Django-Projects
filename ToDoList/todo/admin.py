from django.contrib import admin
from .models import ToDo, Category,Tag
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'isActive',
    
    ]

class ToDoAdmin(admin.ModelAdmin):
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

admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
