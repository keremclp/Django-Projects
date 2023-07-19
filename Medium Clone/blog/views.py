from django.shortcuts import render
from blog.forms import BlogPostModelForm
from blog.models import Category, BlogPost,Tag 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user_profile:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
    
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid oldu...")
            f = form.save(commit=False)
            f.user = request.user
            # f.save()
    
        context = dict(
            form = form
        )
        
    return render(request, 'blog/create_blog_post.html', context)   