from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Post  
from django.db.models import Q


def home(request, category_slug=None):
    categories = None
    post = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        post = Post.objects.filter(category=categories)

    else:
        post = Post.articlemanager.filter(status='published')
    # get query from request
    query = request.GET.get("query")
    # print(query)
    # Set query to '' if None
    if query is None:
        query = ""

    # search for query in headline, sub headline, body
    articles = Post.articlemanager.filter(
        Q(title__icontains=query)
        | Q(sub_title__icontains=query)
        | Q(content__icontains=query)
        # | Q(body__icontains=query)
    )

    context = {"post": post, "articles": articles}

    return render(request, "blog/home.html", context)
