from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .forms import ContactForm


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
