from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from store.models import product
import datetime

# Create your views here.

def store(request):
    products=product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def get(request):
    busqueda=request.GET.get("busqueda")
    result=product.objects.filter(name=busqueda)
    mensaje="EL RESULTADO ES: %s " 
    return HttpResponse(mensaje)
    