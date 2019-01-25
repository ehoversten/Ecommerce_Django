from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
# from apps.accounts.views import login_page, register_page, logout_view, guest_register_view
from apps.accounts.views import login_page, register_page, guest_register_view
from apps.addresses.views import checkout_address_create_view
from .views import home_page, about_page, contact_page

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', home_page, name= 'home'),
    url(r'^admin/', admin.site.urls),
    url(r'^contact$', contact_page, name='contact'),
    url(r'^product/', include('apps.product.urls', namespace= 'product')),
    url(r'^cart/', include('apps.carts.urls', namespace='cart')),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', register_page, name='register'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
]

# for media use
# urlpatterns += staticfiles_urlpatterns()  # this is for any css main files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
