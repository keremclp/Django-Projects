from todo.models import TodoCategory
from page.models import Page
def global_todo_categories_context(request):
    return dict(
        global_todo_categories=TodoCategory.objects.filter(isActive=True)
    )

def global_page_context(request):
    return dict(
        global_pages=Page.objects.filter(isActive=True)
    )