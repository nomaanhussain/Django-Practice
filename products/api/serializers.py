from rest_framework import serializers
from products.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'Title',
            'Description',
            'price',    
            'summary',
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'Title',
            'Description',
            'price',    
            'summary',
        ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'Title',
            'Description',
            'price',    
            'summary',
        ]

