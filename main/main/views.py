from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings

from .forms import ContactForm, LoginForm, RegisterForm

User = settings.AUTH_USER_MODEL

def home_page(request):
	context= {
		"title" : "home"
	}
	return render(request, "home_page.html",context)


def about_page(request):
	context= {
		"title" : "about"

	}
	return render(request, "home_page.html",context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title"	: "contact",
		"form"	: contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	return render(request, "contact.html",context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form' : form
	}
	# print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		# clear form fields
		context['form'] = LoginForm()

	return render(request, "auth/login.html", context)


# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             # Return an 'invalid login' error message.
#             print("Error")
#     return render(request, "login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
