from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from ..views import *
urlpatterns = [
<<<<<<< HEAD
    path('products/<slug:category_slug>/', CategoryFilter.as_view()),
    path('new_products/', New_Products.as_view()),
    path('', view)
=======
    path('', ProductView.as_view()),
    path('new_products/', New_Products.as_view())
>>>>>>> 3fbc4c03ec72598f3a2e688b9145c769d2e09e37
]