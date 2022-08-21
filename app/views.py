from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.conf import settings
import stripe
import json
from .models import *

def index(request):
    """ Loads index page """
    if request.user.is_authenticated:
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
        allBasketItems = basket.get_basket_items
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_items': 0}
        allBasketItems = basket['get_basket_items']
    
    context = {'items':items, 'basket':basket, 'allBasketItems':allBasketItems}
    return render(request, 'app/index.html', context)

def teaStore(request):
    if request.user.is_authenticated:
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
        allBasketItems = basket.get_basket_items
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_items': 0}
        allBasketItems = basket['get_basket_items']
    products = Product.objects.all()
    context = {'products':products, 'allBasketItems':allBasketItems}
    allBasketItems = basket.get_basket_total
    return render(request, 'app/tea-store.html', context)

def potsStore(request):
    if request.user.is_authenticated:
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
        allBasketItems = basket.get_basket_items
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_items': 0}
        allBasketItems = basket['get_basket_items']
    products = Product.objects.all()
    context = {'products':products, 'allBasketItems':allBasketItems}
    allBasketItems = basket.get_basket_total
    return render(request, 'app/pots-and-sets-store.html', context)

def teawareStore(request):
    if request.user.is_authenticated:
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
        allBasketItems = basket.get_basket_items
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_items': 0}
        allBasketItems = basket['get_basket_items']
    products = Product.objects.all()
    context = {'products':products, 'allBasketItems':allBasketItems}
    return render(request, 'app/teaware-store.html', context)

def basket(request):

    if request.user.is_authenticated:
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
        allBasketItems = basket.get_basket_items
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_items': 0}
        allBasketItems = basket['get_basket_items']
    
    context = {'items':items, 'basket':basket, 'allBasketItems':allBasketItems}
    return render(request, 'app/basket.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        customer_info = CustomerInfo.objects.get_or_create(user=customer)
        basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
        items = basket.basketitems_set.all()
        allBasketItems = basket.get_basket_items
    else:
        items = []
        basket = {'get_basket_total': 0, 'get_basket_items': 0}
        allBasketItems = basket['get_basket_items']
    # 'customer_info':customer_info MIGHT NEED TO ADD BACK LATER
    context = {'items':items, 'basket':basket, 'customer_info':customer_info, 'allBasketItems':allBasketItems}
    return render(request, 'app/checkout.html', context)

def updateBasket(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']

    print('Item Id:', itemId)
    print('Action:', action)
    

    customer = request.user
    item = Product.objects.get(id=itemId)
    order, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)

    basketItem, created = BasketItems.objects.get_or_create(order=order, item=item)
    
    if action == 'add':
        basketItem.quantity =  (basketItem.quantity + 1)
    elif action == 'subtract':
        basketItem.quantity =  (basketItem.quantity - 1)

    basketItem.save()

    if basketItem.quantity <= 0:
        basketItem.delete()

    return JsonResponse('Item added to basket', safe=False)

stripe.api_key = settings.STRIPE_SECRET_KEY

# Stripe checkout
class createCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'localhost'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{Product.objects.get(id=itemId)}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })