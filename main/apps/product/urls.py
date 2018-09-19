from django.conf.urls import url
from . import views

 
app_name = 'product'
urlpatterns = [
    # Get routes
    url(r'^$', views.product_landing, name='landing'),
    url(r'^new$', views.product_new, name='new' ), # root page or "landing" page
    url(r'^review$', views.product_review, name='review'), # product review
    url(r'^(?P<product_id>\d+)/detail$', views.producDetail), 
    url(r'^(?P<product_id>\d+)/edit$', views.editProduct), 
    # Post or Put Routes
#    url(r'^/(?P<x>\d+)$/update', views.updateProduct),
#    url(r'^/(?P<x>\d+)$/delete', views.deleteProduct),
] 
# + static(settings.MEDIA_URL, document_root=/main/settings.MEDIA_ROOT) # will need to figure it out later. 

