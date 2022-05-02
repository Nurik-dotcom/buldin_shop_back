from django.urls import path
from .views import *
from ..views import *
urlpatterns = [
    path('products/<slug:category_slug>/', CategoryFilter.as_view()),
    path('new_products/', New_Products.as_view()),
    path('', view)
]