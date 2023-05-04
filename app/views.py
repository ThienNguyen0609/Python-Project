from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    template = loader.get_template('home.html')
    products = Product.objects.all()
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return HttpResponse(template.render(context, request))

def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'cart.html', context)

def Detail(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    product = Product.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {
        'product': product,
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return HttpResponse(template.render(context, request))

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer= customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order= order, product = product)
    if orderItem.quantity == 0:
        if action == 'add':
            orderItem.quantity = 1
            orderItem.save()
    else:
        return JsonResponse("have already added", safe=False)
    return JsonResponse("added", safe=False)

def Inc_Dec_Item(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    order, create = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, create = OrderItem.objects.get_or_create(product=product, order=order)
    if action == 'increase':
        orderItem.quantity+=1
    elif action == 'decrease':
        orderItem.quantity-=1
    orderItem.save()
    if orderItem.quantity == 0:
        orderItem.delete()
    return JsonResponse("Update complete", safe=False)


def Test(request):
    return render(request, 'test.html')