from django.shortcuts import render
from .models import Product, Category



def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)

def show_products(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_id:
        try:
            current_category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=current_category)
        except Category.DoesNotExist:
            current_category = None
            products = Product.objects.all()
    else:
        current_category = None
        products = Product.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category
    }
    return render(request, 'show_products.html', context)
