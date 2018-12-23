from django.contrib import admin
from .models import CategoryProduct, BrandProduct, Product, ProductType

# Register your models here.
admin.site.register(CategoryProduct)
admin.site.register(BrandProduct)
admin.site.register(Product)
admin.site.register(ProductType)
