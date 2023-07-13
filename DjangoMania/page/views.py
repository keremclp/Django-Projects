from django.shortcuts import render
from django.http import HttpResponse,Http404
from .fake_db.pages import FAKE_DB_PAGES

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



def page_view(request,slug):
    result = list(filter(lambda x: (x['url'] == slug), FAKE_DB_PAGES)) 
    
    if result :
        context = dict(
            page_title=result[0]['title'],
            # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
            detail = result[0]['detail'],
        )     
        return render(request, "page/page_detail.html", context)
    else:
        raise Http404
    
   