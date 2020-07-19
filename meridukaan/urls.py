from django.urls import path
from .views import productlist

app_name = 'meridukaan'
urlpatterns = [
    path('', productlist.as_view()),
]

