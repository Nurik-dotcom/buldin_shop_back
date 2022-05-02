from django.shortcuts import render
from .models import *
# Create your views here.

def view(request):
    a = Product.objects.get(id=1)
    context = {'a' : a}
    return render(request, 'index.html', context)
