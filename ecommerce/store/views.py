from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart,cartData,guestOrder
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
# Create your views here.


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('store')
		else:
			# messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	# messages.success(request, ("You Were Logged Out!"))
	return redirect('store')



def cart(request):
    cookieData=cartData(request)
    cartItems=cookieData['cartItems']
    order=cookieData['order']
    items=cookieData['items']
        
    context={'items':items,'order':order,'cartItems':cartItems,'shipping':False}
    
    return render(request,'cart.html',context)


def store(request):
    cookieData=cartData(request)
    cartItems=cookieData['cartItems'] 
    products= Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    
    return render(request,'store.html',context)


def checkout(request):
    cookieData=cartData(request)
    order=cookieData['order']
    items=cookieData['items']
    cartItems=cookieData['cartItems']
        
    context={'items':items,'order':order, 'cartItems':cartItems}
    
    return render(request,'checkout.html',context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('Action:',action)
    print('Product:',productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add': 
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('Item was added',safe=False)
    

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
        )
    else:
        guestorder=guestOrder(request,data)
        order=guestorder['order']
        customer=guestorder['customer']
       
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
        
    if total == float(order.get_cart_total):
            order.complete = True
            order.save()
        
    
    return JsonResponse('Payment complete',safe=False)