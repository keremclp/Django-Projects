from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from blog.models import BlogCategory,BlogTag,Post
# Create your views here.

def all_post_view(request):
    categories = BlogCategory.objects.filter(isActive=True).order_by('title')
    tags = BlogTag.objects.filter(isActive=True).order_by('title')
    all_posts = Post.objects.filter(isActive=True).order_by('-created_at')
    
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = dict(
        categories=categories,
        tags=tags,
        posts=posts,
    )
    return render(request,'blog/all_posts.html',context)

def category_view(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    categories = BlogCategory.objects.filter(isActive=True).order_by('title')
    tags = BlogTag.objects.filter(isActive=True).order_by('title')
    all_posts = Post.objects.filter(
        category = category,
        isActive=True,
    ).order_by('-created_at')

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = dict(
        category=category,
        categories=categories,
        tags=tags,
        posts=posts
    )
    return render(request,'blog/all_posts.html',context)

def tag_view(request, tag_slug):
    tag = get_object_or_404(BlogTag, slug=tag_slug)
    categories = BlogCategory.objects.filter(isActive=True).order_by('title')
    tags = BlogTag.objects.filter(isActive=True).order_by('title')
    posts = Post.objects.filter(
        tag=tag,
        isActive=True,
    ).order_by('-created_at')

    context = dict(
        tag=tag,
        categories=categories,
        tags=tags,
        posts=posts
    )
    return render(request,'blog/all_posts.html',context)

def post_detail_view(request,category_slug, post_slug):
    post = get_object_or_404(Post, slug = post_slug)
    post.view_count = post.view_count + 1 
    post.save()
    categories = BlogCategory.objects.filter(isActive=True).order_by('title')
    tags = BlogTag.objects.filter(isActive=True).order_by('title')


    context = dict(
        post=post,
        categories=categories,
        # category = post.category,
        tags=tags,
    )
    return render(request,'blog/post_detail.html',context)