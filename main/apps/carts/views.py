from django.shortcuts import render, redirect

from .models import Cart
from apps.product.models import Product

#  CREATE CART METHOD
# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print("New Cart Created")
#     return cart_obj

# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        "cart":cart_obj,
    }
    return render(request, "carts/home.html", context)


def cart_update(request):
    # temp product for testing
    print(request.POST)
    # product_id = 5
    product_id = request.POST.get('product_id')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product missing")
            return redirect("cart:home")

        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
        
    return redirect("cart:home")


