from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ This offers the functionality to keep track of whats inside the bag.
     It has a context processor which means it can be accessed
      through all templates throughout the website. """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "product": product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {

        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,

    }

    return context


def save_for_later_contents(request):

    save_for_later_items = []
    save_for_later = request.session.get("save_for_later", {})

    for item_id, quantity in save_for_later.items():
        product = get_object_or_404(Product, pk=item_id)
        save_for_later_items.append({

            "item_id": item_id,
            "product": product,
            "quantity": quantity,
        })

    context = {
        "save_for_later_items": save_for_later_items,


    }

    return context
