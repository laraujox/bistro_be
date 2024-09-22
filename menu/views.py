from rest_framework import generics

from menu.models import Product, Category
from menu.serializers import ProductSerializer, CategorySerializer


class ListProducts(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class ListCategories(generics.ListAPIView):
    queryset = Category.objects.filter(available=True)
    serializer_class = CategorySerializer
