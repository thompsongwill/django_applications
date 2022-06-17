from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.



# def index(request):
#     from django.core.paginator import Pagignator
#     page_obj = goods = Product.objects.all()
'''
            Search option
            
    # product_name = request.GET.get('product_name')
    if product_name != '' and proeduct_name is not None:
            page_obj = goods.filter(title__icontains=product_name)
'''
#     paginator = Paginator(page_obj,6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     
#     context = {'page_obj':page_obj}
#     return render(request, 'store/index.html',context)
#


#class base view for product

class ProductListView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'good'
    paginate_by = 6
    


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/details.html'
    context_object_name = 'product'

# def details(request,product_id):
#     product = Product.objects.get(id=product_id)
#     return render(request, 'store/details.html', {'product':product})



#Class based view to add a product

class AddProductView(CreateView):
    model = Product
    fields = ['title','price','des','image','seller']
    #product_form.html


'''def add_product(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller = request.user
        
        product = Product(seller=seller, title=title, price=price, des=desc, image=image)
        product.save()
    
    return render(request, 'store/addproduct.html') '''


#Update View...



'''def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.des = request.POST.get('desc')
        product.image = request.FILES['upload']
        
        product.save()
        return redirect('store:home')
        
    return render(request, 'store/update_product.html', {'product':product})'''



class UpdateProductView(UpdateView):
    model = Product
    fields = ['title','price','des','image','seller']
    template_name_suffix = '_update_form'
    
    
    

# def delete(request, id):
#     product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('store:listings')
#     return render(request, 'store/delete.html', {'product':product})


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('store:listings')

@login_required
def listings(request):
    products = Product.objects.filter(seller=request.user)
    
    return render(request,'store/listings.html', {'products':products})