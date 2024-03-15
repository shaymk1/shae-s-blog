from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.home, name="home"),
    path("articles/", views.posts, name="articles"),
    path("<slug:post>/", views.single_post, name="post"),
    # path("about/", views.about, name="about"),
]
