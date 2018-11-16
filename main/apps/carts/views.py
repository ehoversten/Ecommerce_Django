from django.shortcuts import render, redirect

from .models import Cart

#  CREATE CART METHOD
def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New Cart Created")
    return cart_obj

# Create your views here.
def cart_home(request):
    #### reset the session variable for testing ####
    # del request.session['cart_id']

    print('*'*50)
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.exists() and qs.count() == 1:
        print('Cart ID exists: ', cart_id)
        print('*'*50)
        cart_obj = qs.first()
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new_cart(user=request.user)
        print("New Cart ID: ", cart_id)
        request.session['cart_id'] = cart_obj.id

    context = {

    }
    return render(request, "carts/home.html", context)
