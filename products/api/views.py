from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView,CreateAPIView
from products.models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


class ProductListAPIView(ListAPIView):   # returns more than one
    queryset = Product.objects.all()  
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView): #returns single object
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'  #default is pk

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(summary= 'okokok')