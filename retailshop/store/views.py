from itertools import product
from django.shortcuts import render, redirect
from .models import Product

# Create your views here.



def index(request):
    goods = Product.objects.all()
    context = {'good':goods}
    return render(request, 'store/index.html',context)



def details(request,product_id):
    product = Product.objects.get(id=product_id)
    
    return render(request, 'store/details.html', {'product':product})