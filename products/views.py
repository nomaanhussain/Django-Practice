from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    DetailView,
    ListView
)
from .models import Product
from .forms import ProductForm, RawProductForm



def product_create_view(requset):


    form = ProductForm(requset.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(requset, 'products/create.html', context)

# def product_create_view(requset):
    
#     my_form = RawProductForm()
#     if requset.method == "POST":
#         my_form = RawProductForm(requset.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)

#     context = {
#         'form': my_form
#     }
#     return render(requset, 'products/create.html', context)

def product_update_view(request, id):
    # initial_data = {
    #     'Title': "My Title"
    # }
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product,id=id)
    # form = ProductForm(request.POST or None, initial=initial_data)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/create.html", context)

def product_detail_view(requset,id):
    print(id)
    obj = Product.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(requset, 'products/details.html', context)



def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        print("dletes")
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "products/delete.html", context)
