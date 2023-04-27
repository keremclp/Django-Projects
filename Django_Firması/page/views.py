from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # print("Result :" ,request)
    return render(request, "page/home_page.html")

def about_us_view(request):
    page_title = "Hakkıssssmızda"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title=page_title,
        hero_content=hero_content
    )
    return render(request,"page/about_us.html",context)


def vision_view(request):
    page_title = "Vizyonumuz"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title=page_title,
    )
    context['hero_content'] = hero_content  
    return render(request,"page/vision.html",context)


def contact_us_view(request):
    page_title = "İletisim"
    hero_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    context = dict(
        page_title=page_title,
        hero_content=hero_content,     
    )
    return render(request,"page/contact_us.html",context)