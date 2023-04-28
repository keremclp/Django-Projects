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
    page_title = "Django"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title = page_title,    
        hero_content = hero_content,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL =FAKE_DB_CAROUSEL
    )
    return render(request, "page/home_page.html",context)

def about_us_view(request):
    page_title = "Hakkıssssmızda"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS     
    )
    return render(request,"page/about_us.html",context)


def vision_view(request):
    page_title = "Vizyonumuz"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title=page_title,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS     
    )
    context['hero_content'] = hero_content  
    return render(request,"page/vision.html",context)


def contact_us_view(request):
    page_title = "İletisim"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS     
    )
    return render(request,"page/contact_us.html",context)

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
    
   