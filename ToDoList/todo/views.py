from django.shortcuts import render
from .models import ToDo
# Create your views here.

def home_view(request):
    todos = ToDo.objects.filter(
        isActive=True,
        # title__icontains ="e"
    )

    context = dict(
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)

