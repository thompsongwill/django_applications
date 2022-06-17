from itertools import product
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    goods = Product.objects.all()
    context = {'good':goods}
    return render(request, 'store/index.html',context)



def details(request,product_id):
    product = Product.objects.get(id=product_id)
    
    return render(request, 'store/details.html', {'product':product})

@login_required
def add_product(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller = request.user
        
        product = Product(seller=seller, title=title, price=price, des=desc, image=image)
        product.save()
    
    return render(request, 'store/addproduct.html')


def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.des = request.POST.get('desc')
        product.image = request.FILES['upload']
        
        product.save()
        return redirect('store:home')
        
    return render(request, 'store/update_product.html', {'product':product})



def delete(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('store:home')
    return render(request, 'store/delete.html', {'product':product})

@login_required
def listings(request):
    products = Product.objects.filter(seller=request.user)
    
    return render(request,'store/listings.html', {'products':products})