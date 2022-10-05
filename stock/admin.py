from django.contrib import admin
import nested_admin

# # Register your models here.
from .models import (
    Category,
    Product,
    Firm,
    Brand,
    Stock
)






# class CategoryAdmin(nested_admin.NestedTabularInline):
#     model=Category
# class BrandAdmin(nested_admin.NestedTabularInline):
#     model=Brand
# class ProductAdmin(nested_admin.NestedModelAdmin):
#     model=Category
#     inlines=[CategoryAdmin,BrandAdmin]


admin.site.register(Firm)
admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Product,ProductAdmin)
admin.site.register(Product)
# admin.site.register(Firm)
admin.site.register(Stock)
