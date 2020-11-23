from django.shortcuts import render


def index(request):
    """ A view that will return you to the index page """
    return render(request, "home/index.html")
