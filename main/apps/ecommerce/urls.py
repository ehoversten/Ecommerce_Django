from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
  url(r'^$', views.mainPage) # this will forward the root page to /product
]
