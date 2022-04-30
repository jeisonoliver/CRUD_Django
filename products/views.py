from django.shortcuts import render, redirect
from .models import product

# Create your views here.

def list_products(request):
    products = product.objects.all( )
    return render (request, 'products.html',{'products' : products})
