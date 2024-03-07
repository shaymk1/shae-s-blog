from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Post


def home(request, category_slug=None):
    categories = None
    post = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        post = Post.objects.filter(category=categories)

    else:
        post = Post.objects.all()
    
    context = {
        "post": post
    }

    return render(request, 'blog/home.html', context)
