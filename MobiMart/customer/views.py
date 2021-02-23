from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
import json
import datetime

from .models import *

# Create your views here.
def checkpass(passw3):
    is_digit=False
    is_upper=False
    is_lower=False
    is_check=False
    is_length=False
    is_special=True
    for i in passw3:
        if i.isupper():
            is_upper=True
        if i.islower():
            is_lower=True
        if i.isdigit():
            is_digit=True
        if not i.isdigit() and not i.isalpha():
            if i!='@' and i!='!' and i!='$':
                is_special=False
    is_check=is_digit and is_lower and is_upper and is_special
    if len(passw3)>=8 and len(passw3)<=20:
        is_length=True
    return is_check and is_length



def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item': 0}
    return render(request,"index.html", {'products':products,'items':items, 'order':order})

def register(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        passw1 = request.POST['password1']
        passw2 = request.POST['password2']
        # print("hello")
        if passw1 == passw2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect("register")
            elif not checkpass(passw1):
                messages.info(request,"1. Must be 8 - 20 characters of length\n2. Must have atleast one capital letters and lowercase letters and numbers\n3. Only accepted @, !, $ (like this type) of characters")
                return redirect("register")


            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=passw1)
                user.save()

                customer = Customer.objects.create(user=user,name=firstname,email=email)
                customer.save()
                return redirect("login")
        
        else:
            messages.info(request,"Password Not Matching")
            print("Password Not Matching")
            return redirect('register')
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')

        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item': 0}

    context = {'items':items, 'order':order}
    return render(request,"checkout.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item': 0}

    context = {'items':items, 'order':order}
    return render(request,"cart.html",context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action ',action)
    print('productId ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    print(data)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order.transaction_id = str(transaction_id)


    total = int(data['form']['total'])
    print(total)
    print(order.get_cart_total)

    if total == order.get_cart_total:
        order.complete = True
    order.save()


    ShippingAdress.objects.create(
        customer=customer,
        order = order,
        address=data['form']['address'],
        city=data['form']['city'],
        state=data['form']['state'],
        zipcode=data['form']['zipcode'],
    )

    return JsonResponse("Payment Complete",safe=False)