from django.shortcuts import render

from products_app.models import Product


# Create your views here.
def show_products(request):
    products = Product.objects.all()
    return render(request, 'show_products.html', context={'product': products})
