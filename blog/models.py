from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# class Author(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200, blank=True, null=True)
#     last_name = models.CharField(max_length=200, blank=True, null=True)


class Post (models.Model):
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(
        null=True, 
        blank=True, 
        upload_to="articles", 
        default="img/placeholder.svg")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    Category = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    time_required_to_read = models.CharField(
        max_length=250, 
        default="2 Min Read"
        )
    is_admin = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ("-date_created",)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
