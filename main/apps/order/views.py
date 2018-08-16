
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from .models import *
import MySQLdb as sql

# Create your views here.
def library(request):
    
    return render(request, 'order/library.html')

def order_detail(request):
    return render(request, 'order/order_detail.html')

def order_list(request):
    return render(request, 'order/order_list.html')
    