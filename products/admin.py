from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "isbn",
        "name",
        "author",
        "num_pages",
        "description",
        "book_format",
        "price",
        "category",
        "rating",
        "publisher",
        "image",
    )

    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
