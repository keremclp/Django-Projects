from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def login_view(request):
    # Login olan kullanıcı direkt olarak ana sayfaya gitsin
    if request.user.is_authenticated:
        # kullanıcıya login olduğunu message olarak belirtmek 
        messages.info(request,f'{request.user.username} already logged in.')
        return redirect('home_view')
    
    context = dict()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username,password)
        # Bilgileri doğru bir şekilde aldık mı ?
        if len(username) < 6 or len(password) < 6 :
            messages.warning(request,'Username or password is too short.')
            return redirect('user_profile:login_view')

        if user is not None:
            login(request, user)
            messages.success(request,f'{user.username} successfully logged in.')
            return redirect('home_view')
            

    return render(request, 'user_profile/login.html',context)

def logout_view(request):
    # kullanıcıya logout olduğunu message olarak belirtmek 
    messages.info(request,f'{request.user.username} successfully logged out.')
    logout(request)
    return redirect('home_view')