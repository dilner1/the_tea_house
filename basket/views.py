from django.shortcuts import render
from .models import Basket
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def basket(request):
    customer = request.user
    basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
    items = basket.basketitems_set.all()
    allBasketItems = basket.get_basket_items
    
    context = {
        'items':items,
        'basket':basket,
        'allBasketItems':allBasketItems
        }
    return render(request, 'app/basket.html', context)

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