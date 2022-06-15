from django.shortcuts import render

def index(request):
    """ Loads index page """
    return render(request, 'home/index.html')
