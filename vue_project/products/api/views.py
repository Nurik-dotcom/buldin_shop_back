from rest_framework import generics
from .serializers import *
from ..models import *  
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()



class New_Products(APIView):
    def get(self, request):
        new_product = Product.objects.order_by('-id')[:4]
        best_seller = Product.objects.order_by('saled')[:4]
        best_seller_serializer = ForFilterSerializer(best_seller, many=True)
        new_product_serailizer = ForFilterSerializer(new_product, many=True)
        context = {
            'Best Seller' : best_seller_serializer.data,
            'New Product' : new_product_serailizer.data
        }
        return Response(context)
