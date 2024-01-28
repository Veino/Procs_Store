from rest_framework import serializers
from .models import Product,ProductCategory, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer(many=False)
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"

