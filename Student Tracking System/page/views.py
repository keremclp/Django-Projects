from django.shortcuts import render

# Create your views here.
def home_view_login(request):
    context = {}
    return render(request, 'page/home_login.html',context)
