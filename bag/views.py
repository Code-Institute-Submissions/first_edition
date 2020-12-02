from django.shortcuts import render


def view_bag(request):
    """ A view that will render the bag """
    return render(request, "bag/bag.html")
