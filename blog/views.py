from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    featured = Post.articlemanager.filter(featured=True)[0:4]

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
    )

    context = {
        "posts": posts,
        "featured": featured,
        "category": category,
        "articles": articles,
    }

    return render(request, "blog/home.html", context)


def posts(request):
    ####### pagination#####
    articles = Post.articlemanager.filter(status="published")[0:4]
    p = Paginator(articles, 4)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get("page")
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {
        "articles": articles,
        "page_obj": page_obj,
    }

    return render(request, "posts/posts.html", context)


def single_post(request, post):
    try:
        post = get_object_or_404(Post, slug=post, status="published")
    except Post.DoesNotExist:
        raise Http404("No article found.")
    context = {"post": post}
    return render(request, "posts/single-post.html", context)


def about(request):
    return render(request, "about/about.html", context)


def contact(request):
    return render(request, "contact/contact.html")
