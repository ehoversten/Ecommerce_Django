from django.conf.urls import url
from . import views
from .views import (Product_landing, )
 
app_name = 'Product'
urlpatterns = [
    # Get routes
    url(r'^$',Product_landing.as_view(), name ='landing'),
    url(r'^new$', views.product_new, name='new' ), # root page or "landing" page
    url(r'^review$', views.product_review, name='review'), # product review
    url(r'^(?P<product_id>\d+)/productDetail$', views.productDetail),
    url(r'^(?P<product_id>\d+)/edit$', views.editProduct),
    # instead of using product id we render product by its slug number
    # url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'), 
    # Post or Put Routes
#    url(r'^/(?P<x>\d+)$/update', views.updateProduct),
#    url(r'^/(?P<x>\d+)$/delete', views.deleteProduct),
] 
# + static(settings.MEDIA_URL, document_root=/main/settings.MEDIA_ROOT) # will need to figure it out later. 

