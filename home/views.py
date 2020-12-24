from django.shortcuts import render, get_object_or_404
from products.models import Product, Category


def index(request):
    """ A view that will return you to the index page """
    product_bestsellers = Product.objects.filter(category=6)
    product_philosophy = Product.objects.filter(category=3)
    product_fiction = Product.objects.filter(category=2)
    product_history = Product.objects.filter(category=1)

    template = "home/index.html"

    context = {
        "product_bestsellers": product_bestsellers,
        "product_philosophy": product_philosophy,
        "product_fiction": product_fiction,
        "product_history": product_history
    }

    return render(request, template, context)
