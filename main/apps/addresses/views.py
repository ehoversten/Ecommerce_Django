from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from apps.billing.models import BillingProfile
from .forms import AddressForm
# Create your views here.


def checkout_address_create_view(request):
    # ----- TESTING ----- #
    print('*'*25)
    print("Landed in Checkout Address Create View!")

    # grab the form
    form = AddressForm(request.POST or None)
    # add form to the page
    context = {
        'form': form
    }

    # HANDELING REDIRECTS
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    # check if form data is valid
    if form.is_valid():
        # ---- TESTING ---- #
        print('*' * 25)
        print(request.POST)

        instance = form.save(commit=False)

        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

        if billing_profile is not None:
            instance.billing_profile = billing_profile
            instance.address_type = request.POST.get('address_type', 'shipping')
            instance.save()
        else:
            print("Error Saving Shipping address")
            return redirect("cart:checkout")

        # Redirect back to checkout page
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("cart:checkout")

    return redirect("cart:checkout")
