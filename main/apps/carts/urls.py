from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.cart_home, name="home"),
    url(r'^update/$', views.cart_update, name="update"),
    url(r'^checkout/$', views.checkout_home, name="checkout"),
]
