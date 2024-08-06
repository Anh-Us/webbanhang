from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.shortcuts import render
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    products = Product.objects.all()
    context= {'products': products }
    return render(request,'app/home.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer =customer,complete =False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'get_cart_items':0,'get_cart_total':0}
    context = {'items': items,'order':order}
    return render(request,'app/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer =customer,complete =False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'get_cart_items':0,'get_cart_total':0}
    context = {'items': items,'order':order}
    return render(request,'app/checkout.html',context)  

#def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer =customer,complete =False)
    orderItem, created = OrderItem.objects.get_or_create(order = order ,product = product)
    if action == 'add':
        OrderItem.quantity +=1
    elif action == 'remove':
        OrderItem.quantity -=1
    OrderItem.save()
    if OrderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('add',safe=False)
# @csrf_exempt
# def updateItem(request):
#     data = json.loads(request.data)
#     productId = data['productId']
#     action = data['action']
#     print("Action",action)
#     print("Pordutcs:",productId)    
#      customer = request.user.customer
#      product = Product.objects.get(id = productId)
#      order, created = Order.objects.get_or_create(customer =customer,complete =False)
#      orderItem, created = OrderItem.objects.get_or_create(order = order ,product = product)
#      if action == 'add':
#          OrderItem.quantity +=1
#      elif action == 'remove':
#         OrderItem.quantity -=1
#      OrderItem.save()
#      if OrderItem.quantity<=0:
#          orderItem.delete()


#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer , complete=False)
#     orderitem, created = orderitem.objects.get_or_create(order= order,product=product)

#     if action == 'add':
#         orderitem.quantity = (orderitem.quantitiy +1)
    
    
#     elif action == 'remove':
#         orderitem.quantity = (orderitem.quantity -1)    
#     orderitem.save()
#     if orderitem.quantity <= 0:
#         orderitem.delete()
#     return JsonResponse("Item was added", safe=False)


#def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action:", action)
    print("ProductId:", productId)
    return JsonResponse("Item was added", safe=False)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
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

    return JsonResponse('Item was updated', safe=False)
