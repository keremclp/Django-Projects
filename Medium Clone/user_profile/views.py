from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from user_profile.models import Profile
from slugify import slugify
from django.contrib.auth.decorators import login_required

from .forms import ProfileModelForm
# Create your views here.

@login_required(login_url='user_profile:login_view')
def profile_edit_view(request):
    user = request.user
    initial_data = dict(
        first_name = user.first_name,
        last_name = user.last_name,
    )
    form = ProfileModelForm(instance= user.profile, initial=initial_data)

    if request.method == "POST":
        form = ProfileModelForm(
            request.POST or None, 
            request.FILES or None, 
            instance= user.profile
        )
        if form.is_valid():
            f = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            f.save()
            messages.success(request,"Profile updated.")
            return redirect('user_profile:profile_edit_view')
        else:
            messages.warning(request,"Profile not updated.")
            return redirect('user_profile:profile_edit_view')

    context = dict(
        form = form,
        title = "Profile Edit",
    )
    return render(request, 'common_components/form.html', context)


def login_view(request):
    # Login olan kullanıcı direkt olarak ana sayfaya gitsin
    if request.user.is_authenticated:
        # kullanıcıya login olduğunu message olarak belirtmek 
        messages.info(request,f'{request.user.username} already logged in.')
        return redirect('home_view')
    
    context = dict()
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

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


def register_view(request):
    context = dict()
    if request.method == "POST":
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')
        

        # print(email,email_confirm, password,password_confirm,first_name,last_name,instagram)
        
        if len(first_name)<3 or len(last_name)<3 or len(email)<3 or len(password)<3:
            messages.warning(request,'Please fill the all fields.')
            return redirect('user_profile:register_view')
        if email != email_confirm :
            messages.warning(request,'Emails are not same.')
            return redirect('user_profile:register_view')

        if password != password_confirm :
            messages.warning(request,'Passwords are not same.')
            return redirect('user_profile:register_view')

        user, created = User.objects.get_or_create(username = email)
        if not created :
            # Niye buraya geldin hacı
            user_login = authenticate(
                request, 
                username=email, 
                password=password
            )
            if user is not None:
                # Email adresi var ve şifre doğru
                messages.success(request,'This email already exists.Going home')
                login(request,user_login)
                return redirect('home_view')
            # Email adresi var ama diyelim ki şifrei yanlış girdi
            messages.warning(request,f'{email} adresi sistemde kayitli ama login olmadiniz. Login sayfasina yönlendirilme .')
            return redirect('user_profile:login_view')
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        

        profile, profile_created = Profile.objects.get_or_create(user=user)
        profile.instagram = instagram
        profile.slug = slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        messages.success(request,f'{user.first_name} Sisteme kayit işlemi tamamlandi .')
        user_login = authenticate(
            request, 
            username=email, 
            password=password
        )
        login(request,user_login)
        return redirect('home_view')
        

    return render(request, 'user_profile/register.html',context)
