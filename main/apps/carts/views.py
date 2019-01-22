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

# Create your views here.
def cart_home(request):
    # grab or the cart object
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

# def checkout_home(request):
#     # grab the cart object
#     print(request)
#     cart_obj, cart_created = Cart.objects.new_or_get(request)
#     # initalize order_obj to null
#     order_obj = None
#     if cart_created or cart_obj.products.count() == 0:
#         return redirect('cart:home')

#     # Initalize Forms
#     login_form = LoginForm()
#     guest_form = GuestForm()
#     address_form = AddressForm()
#     # billing_address_form = AddressForm()

#     # Get or Initalize a Billing Profile with current logged in or guest user
#     billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

#     # IF billing profile already exists
#     if billing_profile is not None:
#         order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

#     context = {
#         "object": order_obj,
#         "billing_profile" : billing_profile,
#         "login_form" : login_form,
#         "guest_form" : guest_form,
#         "address_form" : address_form,
#         "billing_address_form" : billing_address_form
#     }

#     return render(request, 'carts/checkout.html', context)


def checkout_home(request):
    print("Request -> ", request)
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    # user = request.user 
    # billing_profile = None

    # Initalize Forms
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    # Grab the GUEST EMAIL ID from session
    # guest_email_id = request.session.get('guest_email_id')

    # if user.is_authenticated():
    #     billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)

    # elif guest_email_id is not None:
    #     guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
    #     billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email=guest_email_obj.email)
    # else:
    #     print("Guest Login Error")
    #     pass

    if billing_profile is not None:
        order_obj, order_object_created = Order.objects.new_or_get(billing_profile, cart_obj)

        # order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        # if order_qs.count() == 1:
        #     order_obj = order_qs.first()
        # else: 
        #     # old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
        #     # if old_order_qs.exists():
        #     #     old_order_qs.update(active=False)
        #     order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)

    context = {
        "object": order_obj,
        "billing_profile" : billing_profile,
        "login_form" : login_form,
        "guest_form": guest_form,
        "address_form": address_form,
    }

    return render(request, 'carts/checkout.html', context)
