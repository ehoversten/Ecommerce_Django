from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from django.views.generic import TemplateView
# from apps.userAdmin.views import login_page,register_page, guest_register_view
from django.contrib.auth.views import LogoutView
from .views import home_page, about_page, contact_page, login_page, register_page, logout_view

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', home_page, name= 'home'),
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include('apps.product.urls', namespace= 'product')),
    url(r'^cart/', include('apps.carts.urls', namespace='cart')),

    # url(r'^user/', include('apps.loginRegistration.urls')),
    url(r'^customer/', include('apps.customer.urls')),
    # url(r'^order/', include('apps.order.urls')),
    # url(r'^', include('apps.ecommerce.urls')),  # when we hit he root route it will take us there.


    # new login and register logout url nav bar
    url(r'^register/$', register_page, name='register'),
    url(r'^login/$', login_page, name='login'),
    # url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout/$', logout_view, name='logout'),

    # contact navbar
    url(r'^contact$', contact_page, name='contact'),

    # Not implemented yet, but routes are set - Jose 8/13
    # url(r'^review/', include('apps.review.urls')),
    # url(r'^user/', include('apps.loginRegistration.urls')),
    # url(r'^customer/', include('apps.customer.urls')),
    # url(r'^order/', include('apps.order.urls')),

    # we will also need a route for pulling images or have a folder route for it.
]

# for media use
# urlpatterns += staticfiles_urlpatterns()  # this is for any css main files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
