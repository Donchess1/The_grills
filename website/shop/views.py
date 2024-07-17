from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem


def shop(request):
    return render(request, 'shop/shop.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    if created:
        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')

def cart_detail(request):
    cart = get_object_or_404(Cart, id=request.session.get('cart_id'))
    return render(request, 'shop/cart_detail.html', {'cart': cart})
