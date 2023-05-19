from django.shortcuts import render,get_object_or_404
from .models import ToDo, Category
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/admin/login/')
def home_view(request):
    todos = ToDo.objects.filter(
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
    category = get_object_or_404(Category,slug=category_slug)
    todos = ToDo.objects.filter(
        category=category,
        isActive=True,
        user= request.user
    )
    context = dict(
        todos=todos,
        category=category
    )
    return render(request, 'todo/todo_list.html', context)



@login_required(login_url='/admin/login/')
def todo_detail_view(request,category_slug,id):
    todo = get_object_or_404(ToDo,category__slug=category_slug,pk=id, user= request.user)
    context = dict(
        todo=todo 
    )    
    return render(request, 'todo/todo_detail.html',context)


   