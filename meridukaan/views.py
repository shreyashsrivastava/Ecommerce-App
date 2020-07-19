from django.shortcuts import render
from django.views.generic import ListView
from .models import product
# Create your views here.

class productlist(ListView):
    model = product
    context_object_name = 'product_list'
    template_name = 'meridukaan/home.html'

def cart(request):
    return render(request, 'meridukaan/cart.html')

def checkout(request):
    return render(request, 'meridukaan/checkout.html')