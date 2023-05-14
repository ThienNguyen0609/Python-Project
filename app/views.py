from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def searchProduct(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user= user, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "none"
        user_login = "block"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "block"
        user_login = "none"
    x = request.POST.get("search")
    products = Product.objects.filter(name__icontains = x)
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
    }
    return render(request, "search.html", context)

def Register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.info(request, "username has already exist, log in now!")
    context = {
        'form': form
    }
    return render(request, "register.html", context)

def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'username or password is not correct!')
    return render(request, "login.html", {})

def Logout(request):
    logout(request)
    return redirect('home')

def Home(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user= user, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "none"
        user_login = "block"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "block"
        user_login = "none"
    template = loader.get_template('home.html')
    products = Product.objects.all()
    context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
    }
    return HttpResponse(template.render(context, request))

def Cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user= user, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "none"
        user_login = "block"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "block"
        user_login = "none"
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
    }
    return render(request, 'cart.html', context)

def Detail(request, id):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user= user, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "none"
        user_login = "block"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "block"
        user_login = "none"
    product = Product.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {
        'product': product,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
    }
    return HttpResponse(template.render(context, request))

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user= user, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order= order, product = product)
    if action == 'add':
        orderItem.quantity += 1
        orderItem.save()
    return JsonResponse("added", safe=False)

def Inc_Dec_Item(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    user = request.user
    order, create = Order.objects.get_or_create(user=user, complete=False)
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