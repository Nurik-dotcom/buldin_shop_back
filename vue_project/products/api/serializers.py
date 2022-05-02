
from rest_framework import serializers
from ..models import *

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'url']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers
    category = CategorySerializers
    class Meta:
        model = Product
        fields = '__all__'

class ForFilterSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'image','title', 'price']
    # def get_image(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.image.url)

class CategorySerializer(serializers.ModelSerializer):
    products = ForFilterSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            'slug',
            'category', 
            'products',
            'get_absolute_url'
        ]