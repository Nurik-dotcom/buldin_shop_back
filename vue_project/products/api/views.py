from rest_framework import generics
from .serializers import *
from ..models import *  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse

class ProductView(generics.ListAPIView):
    serializer_class = ForFilterSerializer
    queryset = Product.objects.all()
    lookup_field = 'category__sug'

<<<<<<< HEAD
class CategoryFilter(APIView):
    def get_object(self, category_slug):
        return Category.objects.get(slug=category_slug)
    
    def get(self, request, category_slug):
        category = self.get_object(category_slug)  
        serializer = CategorySerializer(category)
        return Response(serializer.data)
     
=======
@csrf_exempt
def tasks(request):
    '''
    List all task snippets
    '''
    if(request.method == 'GET'):
        # get all the tasks
        tasks = Product.objects.all()
        # serialize the task data
        serializer = ForFilterSerializer(tasks, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ForFilterSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

>>>>>>> 3fbc4c03ec72598f3a2e688b9145c769d2e09e37
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
