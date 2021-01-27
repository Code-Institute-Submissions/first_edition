from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view that will return you to the index page """
    product_bestsellers = Product.objects.filter(is_bestseller=True)
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
