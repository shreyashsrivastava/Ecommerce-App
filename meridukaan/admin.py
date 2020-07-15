from django.contrib import admin
from .models import product
# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display = ['product_category','product_name', 'product_price']

admin.site.register(product, productadmin)