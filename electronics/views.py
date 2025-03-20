from django.shortcuts import render, redirect, get_object_or_404
from .models import Product 
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request,'electronics/home.html')


def product_detail(request):
     prod = Product.objects.all()
     form= ProductForm()

     if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form=ProductForm()
     return render(request,'electronics/Product_details.html',{'prod':prod,'form':form})


def update_product(request, id):
     prod = get_object_or_404 (Product, id=id)            #get the product or return 404
     
     if request.method == 'POST':
        form = ProductForm(request.POST ,instance=prod)    #bind tge form to product instance
        if form.is_valid():
            form.save()                                    #save the update products
            return redirect('product_details')              #redirect to the product list after saving 
     else:
        form=ProductForm(instance=prod)                    #populate the form with existing producvt details

     return render(request,'electronics/update_product.html',{'form':form , 'prod':prod})


def delete_product(request, id):
     prod = get_object_or_404 (Product, id=id)             #safe way to get product or return 404 not found
     prod.delete()
     return redirect('product_details')                     #redirect back to product details page after deletion

    