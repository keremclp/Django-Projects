from django.urls import path
from todo.views import all_todos_view,category_view,tag_view,todo_detail_view


urlpatterns = [
    #All todos
    path('', all_todos_view, name='all_todos_view'),

    #Category and Tag views
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>', tag_view, name='tag_view'),

    #Todo-detail
    path('category/<slug:category_slug>/todo/<int:id>/', todo_detail_view, name='todo_detail_view'),
]