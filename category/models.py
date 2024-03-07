from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    # for the category to show products when clicked on:
    def get_url(self):
        return reverse("articles_by_category", args=[self.slug])

    def __str__(self):
        return self.category_name

