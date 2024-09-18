from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product

class Home(ListView):
    model = Product
    template_name = 'home/base.html'
    context_object_name = 'products'

