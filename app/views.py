from django.shortcuts import render
from .models import *

def index(request):
    """ Loads index page """
    return render(request, 'app/index.html')

def teaStore(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'app/tea-store.html', context)

def potsStore(request):
    products = Product.object.all()
    context = {'products':products}
    return render(request, 'app/pots-and-sets-store.html', context)

def teawareStore(request):
    products = Product.object.all()
    context = {'products':products}
    return render(request, 'app/teaware-store.html', context)

def basket(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        # order, created = BasketItems.objects.get_or_create(customer=customer)
        items = BasketItems.item
    else:
        items = []
    context = {'items':items}
    return render(request, 'app/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)