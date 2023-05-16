from django.contrib import admin
from .models import ToDo
# Register your models here.


class ToDoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'isActive',
        # 'created_at',
        # 'updated_at', 
    ]


admin.site.register(ToDo, ToDoAdmin)

