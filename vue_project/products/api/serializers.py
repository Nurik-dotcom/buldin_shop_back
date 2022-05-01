from dataclasses import field
from rest_framework import serializers
from ..models import *

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'url']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'type']

class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers
    category = CategorySerializers
    class Meta:
        model = Product
        fields = '__all__'

class ForFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image','title', 'price']

