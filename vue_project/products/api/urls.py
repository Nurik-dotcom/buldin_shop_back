from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('new_products/', New_Products.as_view())
]