from django.shortcuts import render
from .models import Product
# Create your views here.
from .forms import ProductForm

def product_create_view(requset):
    form = ProductForm(requset.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(requset, 'products/create.html', context)

def product_detail_view(requset):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(requset, 'products/details.html', context)