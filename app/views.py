from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import stripe
import json
from .models import NewsletterSignup
from basket.models import Basket
from checkout.models import BasketItems, CustomerInfo
from .forms import NewsletterSignupForm

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
    
    context = {
        'items':items,
        'basket':basket,
        'allBasketItems':allBasketItems
        }
    return render(request, 'app/index.html', context) 


# @login_required(login_url='/accounts/login/')
# def checkout(request, *args, **kwargs):
#     print(request.method)
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY
#     stripe.api_key = stripe_secret_key

#     # pk = request.GET.get('pk')
#     customer = request.user
#     form = CustomerInfoForm()
#     basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
#     items = basket.basketitems_set.all()
#     allBasketItems = basket.get_basket_items

# # BasketItems
# #     item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
# #     order = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True)
# #     quantity = models.IntegerField(default=0, null=True, blank=True)
# #     added_date = models.DateTimeField(auto_now_add=True, max_length=150)

# #     @property
# #     def add_total(self):
# #         total = self.item.price * self.quantity
# #         return total

#     if request.method == 'POST':
#         form = CustomerInfoForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.creator = request.user
#             event = form.save()

#             price = 2

#             checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price': price,
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url='/success/',
#             cancel_url='/cancel/',
#         )
#             return redirect(checkout_session.url)
#             # return HttpResponseRedirect(reverse('success'))
#         else:
#             print("ERROR : ", form.errors)
#     context = {
#         'items': items,
#         'basket': basket,
#         'form': form,
#         'allBasketItems': allBasketItems,
#         'stripe_public_key': stripe_secret_key,
#         'client_secret': 'test client secret',
#         }
#     return render(request, 'app/checkout.html', context)

def NewsletterSignupView(request):

    form = NewsletterSignupForm(request.POST or None)
    print('checking email address')
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSignup.objects.filter(email=instance.email).exists():
            print('removing email address')
            NewsletterSignup.objects.filter(email=instance.email).delete()
        else:
            instance.save()

    context = {
        'form': form
    }
    return render(request, "app/my_account.html", context)


# def successView(request):
#     context = {}
#     return render(request, "app/success.html/", context)

# def cancelView(request):
#     context={}
#     return render(request, "app/cancel.html/", context)

def handler404View(request, exception):
    return render(request, '404.html', status=404)