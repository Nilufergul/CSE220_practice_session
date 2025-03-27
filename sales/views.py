from django.shortcuts import render, redirect
from .models import Cart
from products_app.models import Product
from django.contrib import messages


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    cart_items = Cart.objects.filter(product=product)
    
    if cart_items.exists():
        cart_item = cart_items.first()
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.error(request, 'Insufficient stock available.')
            return redirect('/products/')
    else:
        cart_item = Cart(product=product, quantity=1)
        cart_item.save()
    
    return redirect('cart_detail')

def cart_detail(request):
    cart_items = Cart.objects.all()
    return render(request, 'sales/cart_detail.html', {'cart_items': cart_items})

def remove_from_cart(request, product_id):
    cart_item = Cart.objects.filter(product_id=product_id).last()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, 'Product quantity reduced.')
        else:
            cart_item.delete()
            messages.success(request, 'Product removed from cart.')
    else:
        messages.error(request, 'Product not found in your cart.')
    return redirect('cart_detail')
