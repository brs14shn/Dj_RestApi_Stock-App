from django.shortcuts import render

from .models import (
    Category,
    Brand,
    Product,
    Stock,
    Firm
)
from .serializers import (
    CategorySerializers,
    BrandSerializers,
)

from rest_framework import generics 

from rest_framework.viewsets import ModelViewSet


class CategoryViewListCreate(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers

class CategoryURD(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers


class BrandViewSet(ModelViewSet):
     queryset=Brand.objects.all()
     serializer_class=BrandSerializers