from django.contrib import admin
from django.urls import path
from products.api.views import (
    ProductListAPIView,
    ProductDetailAPIView, 
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductCreateAPIView,
)
urlpatterns = [
    path('get_products/', ProductListAPIView.as_view(), name='product'),
    path('get_product/<pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    # path('get/<price>', ProductDetailAPIView.as_view(), name='product_detail'),  ## searching based on price
    path('update_product/<pk>', ProductUpdateAPIView.as_view(), name='update_product'),
    path('delete_product/<pk>', ProductDeleteAPIView.as_view(), name='delete_product'),
    path('create_product/', ProductCreateAPIView.as_view(), name='create_product'),
]
