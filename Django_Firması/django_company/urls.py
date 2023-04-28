"""
URL configuration for django_company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     print(request)
#     return HttpResponse("Hello, world. You're at the polls index.")

# Danışma :)
urlpatterns = [
    path('', include('page.urls'),), # PAGE APPLICATION içindeki urls.py den alıyoruz...
    path('admin/', admin.site.urls),
]