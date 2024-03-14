from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from django.urls import reverse


class Profile(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile")
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += " " + str(self.last_name)
        return name


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(
        null=True, blank=True, upload_to="articles", default="img/placeholder.svg"
    )
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="post_author", default="author"
    )
    time_required_to_read = models.CharField(max_length=250, default="2 Min Read")
    is_admin = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=options, default="draft")
    content = models.TextField(default="")
    featured = models.BooleanField(default=False)

    articlemanager = ArticleManager()  # custom manager

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-date_created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
