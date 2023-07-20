from django.shortcuts import redirect, render
from blog.forms import BlogPostModelForm
from blog.models import Category, BlogPost, Tag
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
# Create your views here.


@login_required(login_url='user_profile:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
    context = dict(
        form = form
    )
    
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid oldu...")
            f = form.save(commit=False)
            print(form.cleaned_data)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title = item.get('value'))
                f.tag.add(tag_item)
            messages.success(request,"Blog kaydedildi")
            return redirect('home_view')
    

    return render(request, 'blog/create_blog_post.html', context)
