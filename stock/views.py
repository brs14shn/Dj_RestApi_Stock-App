from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly

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
    ProductSerializers,
    FirmSerializers,
    StockSerializers,
    

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

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

class FirmViewSet(ModelViewSet):
    queryset=Firm.objects.all()
    serializer_class=FirmSerializers

class StockViewSet(ModelViewSet):
    queryset=Stock.objects.all()
    serializer_class=StockSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
