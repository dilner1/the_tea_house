from django.shortcuts import render

def index(request):
    """ Loads index page """
    return render(request, 'app/index.html')

def teaStore(request):
    context = {}
    return render(request, 'app/tea-store.html', context)

def potsStore(request):
    context = {}
    return render(request, 'app/posts-store.html', context)

def setsStore(request):
    context = {}
    return render(request, 'app/sets-store.html', context)

def basket(request):
    context = {}
    return render(request, 'app/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)