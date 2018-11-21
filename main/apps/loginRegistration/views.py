# from __future__ import unicode_literals
# from .models import User
# from django.contrib.messages import error
# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib import messages
# from .models import *
# import datetime
# import MySQLdb as sql
#
#
# def index(request):
#     try:
#         request.session['user_id']
#     except:
#         request.session['user_id'] = []
#     if request.session['user_id']:
#         return redirect('/user/success')
#     return render(request, "loginRegistration/index.html")
#
#
# def create(request):
#     if request.method == 'POST':
#         result = User.objects.validation(request.POST)
#     if type(result) == list:
#         for error in result:
#             messages.error(request, error)
#         return redirect('/')
#     request.session['user_id'] = result.id
#     messages.success(request, "Successfully Registered")
#     return redirect('/user/success')
#
#
# def login(request):
#     result = User.objects.validation_2(request.POST)
#     if type(result) == list:
#         for error in result:
#             messages.error(request, error)
#         return redirect('/user')
#
#     request.session['user_id'] = result.id
#     messages.success(request, "Thanks for logging in!")
#     return redirect('/user/success')
#
#
# def success(request):
#     try:
#         request.session['user_id']
#     except:
#         return redirect('/')
#     context = {
#         "user": User.objects.get(id=request.session['user_id'])
#     }
#     return render(request, "loginRegistration/success.html", context)
#
#
# def logout(request):
#     request.session.clear()
#     return render(request, "loginRegistration/index.html")
