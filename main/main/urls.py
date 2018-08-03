from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.ecommerce.urls')),
    url(r'^', include('apps.loginRegistration.urls')),
    url(r'^', include('apps.product.urls')),
]
