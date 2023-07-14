from django.shortcuts import get_object_or_404, render
from page.models import Page

# FAKE_DB_PROJECTS = [
#     f"https://picsum.photos/id/{id}/100/80" for id in range(21,29)
# ] 

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(24,28)
]

# Create your views here.
def home_view(request):
    # print("Result :" ,request)
    
    context = dict(
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL =FAKE_DB_CAROUSEL
    )
    return render(request, "page/home_page.html",context)


def page_view(request,page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = dict(
        page=page
    )
    return render(request,"page/page_detail.html",context)
