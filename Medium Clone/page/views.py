from django.shortcuts import render
from blog.models import BlogPost,Tag,Category
# Create your views here.
def home_view(request):
    posts = BlogPost.objects.filter(isActive=True)
    tags = Tag.objects.filter(isActive=True)
    categories = Category.objects.filter(isActive=True)
    context = dict(
        posts = posts,
        tags = tags,
        categories = categories,
    )
    return render(request, 'page/home_page.html',context)
