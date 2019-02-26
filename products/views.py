from django.shortcuts import render
from .models import Product
# Create your views here.

def product_detail_view(requset):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(requset, 'products/details.html', context)