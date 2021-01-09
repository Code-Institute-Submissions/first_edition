from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that will render the bag """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the  product to the  bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f"Updated {product.name} \
                 Quantity in your bag to {bag[item_id]}")
    else:
        bag[item_id] = quantity
        messages.success(request, f"Added {product.name} to your bag")

    request.session['bag'] = bag
    return redirect(redirect_url)


def add_to_save_for_later(request, item_id):
    """ Saves a product in the bag template
     for later purchase but doesn't actually add to shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get("redirect_url")
    save_for_later = request.session.get("save_for_later", {})

    if item_id in list(save_for_later.keys()):
        messages.success(
            request, f"The book {product.name} \
                is already saved for later")
    else:
        save_for_later[item_id] = quantity
        messages.success(
            request, f"Added {product.name} to your saved for later items")

    request.session['save_for_later'] = save_for_later
    return redirect(redirect_url)


def remove_from_saved(request, item_id):
    """Remove the item from the saved items"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        save_for_later = request.session.get("save_for_later", {})
        save_for_later.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your saved items')
        request.session['save_for_later'] = save_for_later
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def remove_from_saved_no_toast(request, item_id):
    """Remove the item from the saved items"""

    try:
        save_for_later = request.session.get("save_for_later", {})
        save_for_later.pop(item_id)
        request.session['save_for_later'] = save_for_later
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def adjust_bag(request, item_id):
    """update the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} \
                 Quantity in your bag to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} \
             from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get("bag", {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
