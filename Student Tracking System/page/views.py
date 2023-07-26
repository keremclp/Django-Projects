from django.shortcuts import render

# Create your views here.
def home_view_login(request):
    if request.method == "POST" :
        print(request.POST)
        
    return render(request, 'page/home_login.html',{})
