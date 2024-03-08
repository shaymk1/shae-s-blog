from django.shortcuts import render
# from django.db.models import Q
# from blog.models import Post


def category(request):
    
    return render(request, 'category/categories-grid.html')
