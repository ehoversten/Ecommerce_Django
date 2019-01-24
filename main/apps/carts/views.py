from django.shortcuts import render, redirect
# Import Forms
from apps.accounts.forms import LoginForm, GuestForm
from apps.addresses.forms import AddressForm
# Import Models
from .models import Cart
from apps.orders.models import Order
from apps.product.models import Product
from apps.accounts.models import GuestEmail
from apps.billing.models import BillingProfile
from apps.addresses.models import Address

# Create your views here.
def cart_home(request):
    # grab or create the cart object
    cart_obj, cart_created_obj = Cart.objects.new_or_get(request)
    context = {
        "cart": cart_obj,
    }
    return render(request, "carts/home.html", context)

def cart_update(request):
    # Grab the Product ID
    product_id = request.POST.get('product_id')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Product missing from Database")
            return redirect("cart:home")
        # Grab or create CART object
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
        
    return redirect("cart:home")

def checkout_home(request):
    # Create or Grab the cart object
    print(request)
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    # initalize order_obj to null
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')

    # Initalize Forms
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    # billing_address_form = AddressForm()

    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    # Get or Initalize a Billing Profile with current logged in or guest user
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    # IF billing profile already exists
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        # IF shipping_address exists
        if shipping_address_id:
            # Associate ORDER OBJECT to shipping address
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            # Remove shipping_address_id from session 
            del request.session["shipping_address_id"]
        # IF billing_address exists
        if billing_address_id:
            # Associate ORDER OBJECT to billing address
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            # Remove billing_address_id from session
            del request.session["billing_address_id"]
        # IF either exist -> save()
        if billing_address_id or shipping_address_id:
            order_obj.save()


    if request.method == 'POST':
        # create variable to run method to verify ORDER contains all needed information 
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            # reset cart_items in session 
            request.session['cart_items'] = 0
            # remove from session 
            del request.session['cart_id']
            return redirect("/cart/success")


    context = {
        "object": order_obj,
        "billing_profile" : billing_profile,
        "login_form" : login_form,
        "guest_form" : guest_form,
        "address_form" : address_form,
        # "billing_address_form" : billing_address_form
    }

    return render(request, 'carts/checkout.html', context)


# def checkout_home(request):
#     print("Request -> ", request)
#     cart_obj, cart_created = Cart.objects.new_or_get(request)
#     order_obj = None
#     if cart_created or cart_obj.products.count() == 0:
#         return redirect("cart:home")

#     # user = request.user 
#     # billing_profile = None

#     # Initalize Forms
#     login_form = LoginForm()
#     guest_form = GuestForm()
#     address_form = AddressForm()

#     billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

#     if billing_profile is not None:
#         order_obj, order_object_created = Order.objects.new_or_get(billing_profile, cart_obj)

#     context = {
#         "object": order_obj,
#         "billing_profile" : billing_profile,
#         "login_form" : login_form,
#         "guest_form": guest_form,
#         "address_form": address_form,
#     }

#     return render(request, 'carts/checkout.html', context)
