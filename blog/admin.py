from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "sub_title",
        "category",
        "slug",
        "author",
        "date_created",
    )
    list_filter = (
        "author",
        "title",
        "category"
    )
    prepopulated_fields = {"slug": ("title",), }
    # prepopulated_fields = {'slug': ('title',), }


admin.site.register(Post)
