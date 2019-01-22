from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail

User = settings.AUTH_USER_MODEL
# Create your views here.

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form,
    }

    # HANDELING REDIRECTS
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    # check if form data is valid
    if form.is_valid():
        # Grab the validated email
        email = form.cleaned_data.get("email")
        # Create a new GuestEmail obj -> assign email
        new_guest_email = GuestEmail.objects.create(email=email)
        # Put the guest ID in session
        request.session['guest_email_id'] = new_guest_email.id
        # Redirect back to prior page before guest login required
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')

    return redirect('/register/')


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }

    # HANDELING REDIRECTS
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    # check if form data is valid
    if form.is_valid():
        # Initalize variables for binding form data
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # User exists -> (?)
        if user is not None:
            login(request, user)

            # if user is logged in we can void the 'guest_email_id' stored in request.session
            try:
                del request.session['guest_email_id']
            except:
                pass
            
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print("Error... Invalid Login, Please Try again")

    return render(request, "accounts/login.html", context)


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('/')


# Grab the USER model
User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form': form,
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		# create newly registered user
		new_user = User.objects.create_user(username, email, password)
		print(new_user)

	return render(request, 'accounts/register.html', context)
