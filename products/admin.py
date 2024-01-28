from django.contrib import admin
from .models import Product, ProductCategory, ProductImage

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(ProductCategory)