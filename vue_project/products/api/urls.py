from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', ProductView.as_view()),
    path('new_products/', New_Products.as_view())
]