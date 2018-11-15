from django.shortcuts import render, redirect

# Create your views here.
def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        print("create new cart")
        request.session['cart_id'] = 5
    else:
        print('Cart ID exists: ', cart_id)
    # if user is logged in assign to session
    # request.session['user'] = request.session.username

    context = {

    }
    return render(request, "carts/home.html", context)