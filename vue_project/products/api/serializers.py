
from rest_framework import serializers
from ..models import *

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'url']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
<<<<<<< HEAD
        fields = ['category', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
=======
        fields = ['category',]
>>>>>>> 3fbc4c03ec72598f3a2e688b9145c769d2e09e37

class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers
    category = CategorySerializers
    class Meta:
        model = Product
        fields = '__all__'

class ForFilterSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    # image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'image','title', 'price']
    # def get_image(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.image.url)
=======
    category = CategorySerializers()
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Product
        fields = ['id', 'image','title', 'price', 'category']

    # def get_image_url(self, product):
    #     request = self.context.get('request')
    #     image_url = product.image.url
    #     return request.build_absolute_uri(image_url)
>>>>>>> 3fbc4c03ec72598f3a2e688b9145c769d2e09e37

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