from django.shortcuts import render


def category(request):
    return render(request, 'category/categories-grid.html')
