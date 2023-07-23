from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from blog.forms import BlogPostModelForm
from blog.models import Category, BlogPost, Tag, UserPostFav
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
# Create your views here.


@login_required(login_url='user_profile:login_view')
def fav_update_view(request):
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, slug=request.POST.get('slug'))
        if (post):
            post_fav, created = UserPostFav.objects.get_or_create(
                user=request.user,
                post=post,
            )
            if not created:
                post_fav.is_deleted = not post_fav.is_deleted
                post_fav.save()

    return JsonResponse({'status': 200})


@login_required(login_url='user_profile:login_view')
def create_blog_post_view(request):
    title = "Yeni Blog Post :"
    form = BlogPostModelForm()
    context = dict(
        title=title,
        form=form
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
                tag_item, created = Tag.objects.get_or_create(
                    title=item.get('value')).lower()
                f.tag.isActive = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Blog kaydedildi")
            return redirect('home_view')

    return render(request, 'common_components/form.html', context)


@login_required(login_url='user_profile:login_view')
def post_edit_view(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)

    if not post.user == request.user:
        messages.warning(request, "You can n ot edit this blog")
        return redirect('home_view')

    title = post.title
    form = BlogPostModelForm(instance=post)

    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None,
                                 request.FILES or None, instance=post)
        if form.is_valid():
            print("Valid oldu...")
            f = form.save(commit=False)
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(
                    title=item.get('value').lower())
                f.tag.isActive = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Blog düzenlendi")
            return redirect('home_view')

    context = dict(
        title=title,
        form=form
    )
    return render(request, 'common_components/form.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = dict(
        category=category,
    )
    return render(request, 'blog/post_list.html', context)


def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = BlogPost.objects.filter(tag=tag)

    context = dict(
        tag=tag,
    )
    return render(request, 'blog/post_list.html', context)
