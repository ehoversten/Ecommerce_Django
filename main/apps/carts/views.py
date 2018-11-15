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
    # if cart_id is None:
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    #     # print('*'*50)
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.exists and qs.count == 1:
        print('Cart ID exists: ', cart_id)
        print('*'*50)
        cart_obj = qs.first()
    else:
        cart_obj = cart_create()
        print("New Cart ID: ", cart_id)
        request.session['cart_id'] = cart_obj.id

    context = {

    }
    return render(request, "carts/home.html", context)
