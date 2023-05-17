from django.shortcuts import render,get_object_or_404
from .models import ToDo
from django.http import Http404
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


# def todo_detail_view(request,id):
#     try:
#         todo = ToDo.objects.get(pk=id)
#         context = dict(
#             todo=todo
#         )    
#         return render(request, 'todo/todo_detail.html',context)
#     except ToDo.DoesNotExist:
#         raise Http404 
def todo_detail_view(request,id):
    todo = get_object_or_404(ToDo,pk=id)
    context = dict(
        todo=todo
    )    
    return render(request, 'todo/todo_detail.html',context)
   