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


def add_product(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        
        product = Product(title=title, price=price, des=desc, image=image)
        product.save()
    
    return render(request, 'store/addproduct.html')


def update_product(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'store/update_product.html', {'product':product})