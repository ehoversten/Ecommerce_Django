from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('apps.loginRegistration.urls')), 
    url(r'^product/', include('apps.product.urls')),
    url(r'^customer/', include('apps.customer.urls')),
    url(r'^', include('apps.ecommerce.urls')),  # when we hit he root route it will take us there.

    # Not implemented yet, but routes are set - Jose 8/13
    # url(r'^review/', include('apps.review.urls')),
    # url(r'^order/', include('apps.order.urls')),

    # we will also need a route for pulling images or have a folder route for it. 
]
