from django.urls import path
from .views import list_products

urlpartterns = [
    path('', list_products, name='list_products'),
]