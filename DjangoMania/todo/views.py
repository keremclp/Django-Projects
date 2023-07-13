from django.shortcuts import render,get_object_or_404
from .models import Todo, TodoCategory,TodoTag
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/admin/login/')
def all_todos_view(request):
    todos = Todo.objects.filter(
        user=request.user,
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

@login_required(login_url='/admin/login/')
def category_view(request, category_slug):
    category = get_object_or_404(TodoCategory,slug=category_slug)
    todos = Todo.objects.filter(
        category=category,
        isActive=True,
        user= request.user
    )
    context = dict(
        category=category,
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)



@login_required(login_url='/admin/login/')
def todo_detail_view(request,category_slug,id):
    todo = get_object_or_404(Todo, category__slug=category_slug, pk=id, user= request.user)
    context = dict(
        todo=todo 
    )    
    return render(request, 'todo/todo_detail.html',context)

@login_required(login_url='/admin/login/')
def tag_view(request, tag_slug):
    tag = get_object_or_404(TodoTag,slug=tag_slug,)
    context = dict(
        tag=tag,
        todos=tag.todo_set.filter(user=request.user)
    )
    return render(request, 'todo/todo_list.html', context)

   