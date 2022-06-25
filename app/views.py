from django.shortcuts import render

def index(request):
    """ Loads index page """
    return render(request, 'app/index.html')

def teaStore(request):
    context = {}
    return render(request, 'app/tea-store.html', context)

def potsStore(request):
    context = {}
    return render(request, 'app/pots-and-sets-store.html', context)

def teawareStore(request):
    context = {}
    return render(request, 'app/teaware-store.html', context)

def basket(request):
    context = {}
    return render(request, 'app/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)