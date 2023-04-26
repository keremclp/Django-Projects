from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # print("Result :" ,request)
    return render(request, "page/home_page.html")

def about_us_view(request):
    context = dict()
    return render(request,"page/about_us.html",context)

def contact_us_view(request):
    context = dict()
    return render(request,"page/contact_us.html",context)