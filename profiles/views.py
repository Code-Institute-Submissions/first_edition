from django.shortcuts import render


def profile(request):

    """ A view that will bring the user to their profile page """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
