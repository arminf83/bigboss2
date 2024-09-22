# class base
# from django.shortcuts import render
# from django.views.generic import ListView
# from product.models import Product

# class Home(ListView):
#     model = Product
#     template_name = 'home/base.html'
#     context_object_name = 'products'

from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product , Category

def home (request):
    product = Product.objects.order_by('-id')[4:13]
    category = Category.objects.all()
    newproducts = Product.objects.order_by('-id')[:3]  # دریافت ۳ محصول آخر
    product_1 = newproducts[0] if len(newproducts) > 0 else None
    product_2 = newproducts[1] if len(newproducts) > 1 else None
    product_3 = newproducts[2] if len(newproducts) > 2 else None
    
    
    return render(request,'home/indexx.html',context={
        'categories': category,
        'product_1': product_1,
        'product_2': product_2,
        'product_3': product_3,
        'products': product
        })