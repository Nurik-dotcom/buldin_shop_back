"""vue_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
=======

>>>>>>> 3fbc4c03ec72598f3a2e688b9145c769d2e09e37
urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('products.api.urls')),
    path('user/', include('users.api.urls'))
<<<<<<< HEAD
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 3fbc4c03ec72598f3a2e688b9145c769d2e09e37
