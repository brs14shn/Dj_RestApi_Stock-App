from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Product,
    Stock,
    Firm
)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"

class ProductSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField() # sadece read-only
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields=(
            "id",
            "product_name",
            "category",
            "brand",
            "stock_quantity",

        )

class FirmSerializers(serializers.ModelSerializer):
   
    class Meta:
        model=Firm
        fields=(
            "id",
            "firm_name",
            "phone_number",
            "address",
        )
class StockSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField() # sadece read-only
    product=serializers.StringRelatedField() 
    firm=serializers.StringRelatedField()
    user_id=serializers.IntegerField(write_only=True)
    firm_id=serializers.IntegerField(write_only=True)
    product_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Stock
        fields=(
            "id",
            "user",
            "user_id", # post
            "firm",
             "firm_id", # post
            "transaction",
            "product",
            "product_id",  # post
            "quantity",
            "price",
            "price_total"
        )
