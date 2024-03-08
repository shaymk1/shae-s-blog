from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Post
from django.db.models import Q


def home(request, category_slug=None):
    # to get category_slug
    categories = None
    posts = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=categories)

    else:
        posts = Post.articlemanager.filter(status="published")[0:4]

    # to get category-list
    category = Category.objects.all()
    # get query from request
    query = request.GET.get("query")
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

    featured = Post.articlemanager.filter(featured=True)[0:4]

    context = {
        "posts": posts,
        "articles": articles,
        "featured": featured,
        "category": category,
    }

    return render(request, "blog/home.html", context)
