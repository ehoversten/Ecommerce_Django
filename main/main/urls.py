from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.userAdmin.views import login_page,register_page, guest_register_view
from django.contrib.auth.views import LogoutView
from .views import home_page, about_page, contact_page
from django.conf import settings

urlpatterns = [
    url(r'^$', home_page, name= 'home'),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('apps.loginRegistration.urls')), 
    # url(r'^product/', include('apps.product.urls')),
    url(r'^customer/', include('apps.customer.urls')),
    url(r'^', include('apps.ecommerce.urls')),  # when we hit he root route it will take us there.
    # url(r'^order/', include('apps.order.urls')),

    # new login and register logout url nav bar
    url(r'^register/$', register_page,name='register'),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # contact navbar
    url(r'^contact/$', contact_page, name='contact'),

    # Not implemented yet, but routes are set - Jose 8/13
    # url(r'^review/', include('apps.review.urls')),
    
    # we will also need a route for pulling images or have a folder route for it. 
]

# for media use
# if settings.DEBUG:
#     urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)