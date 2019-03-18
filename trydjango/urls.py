"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from products.views import product_detail_view, product_create_view, product_update_view, product_delete_view

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('create/', product_create_view),
    path('product/<int:id>/update/', product_update_view),
    path('product/<int:id>/delete/', product_delete_view),
    path('product/<int:id>/', product_detail_view,name="product-detail-view"),
    path('', home_view, name = 'home'),
    path('admin/', admin.site.urls),
    path('product/api/', include('products.api.urls')),
]
