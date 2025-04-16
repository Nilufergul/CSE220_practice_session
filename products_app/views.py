from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q
from .forms import SearchForm



def home(request):
    categories = Category.objects.all()
    search_form = SearchForm()
    context = {
        'categories': categories,
        'search_form': search_form,
    }
    return render(request, 'home.html', context)

def show_products(request):
    category_id = request.GET.get('category')
    search_query = request.GET.get('search')
    categories = Category.objects.all()
    search_form = SearchForm(request.GET)
    
    products = Product.objects.all()
    
    if category_id:
        try:
            current_category = Category.objects.get(id=category_id)
            products = products.filter(category=current_category)
        except Category.DoesNotExist:
            current_category = None
    else:
        current_category = None
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
        'search_form': search_form
    }
    return render(request, 'show_products.html', context)
