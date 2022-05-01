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
        fields = ['category',]

class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers
    category = CategorySerializers
    class Meta:
        model = Product
        fields = '__all__'

class ForFilterSerializer(serializers.ModelSerializer):
    category = CategorySerializers()
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Product
        fields = ['id', 'image','title', 'price', 'category']

    # def get_image_url(self, product):
    #     request = self.context.get('request')
    #     image_url = product.image.url
    #     return request.build_absolute_uri(image_url)

