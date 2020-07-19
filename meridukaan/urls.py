from django.urls import path
from .views import productlist, cart
from . import views

app_name = 'meridukaan'
urlpatterns = [
    path('', productlist.as_view(), name='home'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]

