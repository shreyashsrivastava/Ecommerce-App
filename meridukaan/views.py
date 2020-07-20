from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class productlist(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'meridukaan/home.html'

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}

    for_front = {
        'items':items,
        'order':order,
    }
    return render(request, 'meridukaan/cart.html', for_front)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}

    for_front = {
        'items':items,
        'order':order,
    }
    return render(request, 'meridukaan/checkout.html', for_front)