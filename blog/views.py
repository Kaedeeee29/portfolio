from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag


def post_list(request):
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')

    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'active_category': category_slug,
        'active_tag': tag_slug,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    related_posts = Post.objects.filter(
        published=True, category=post.category
    ).exclude(pk=post.pk)[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)
