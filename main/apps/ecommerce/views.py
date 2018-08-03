from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def mainPage(request):
    return redirect('product/')
