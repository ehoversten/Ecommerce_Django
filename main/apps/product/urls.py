from django.conf.urls import url
from . import views


""" Meggie, you can just test the pages by changing the landing return on views to whichever page you're designing, I will take of the logic afterwords -Jose 8/13  """
urlpatterns = [

    # Get routes
    url(r'^$', views.landing), # root page or "landing" page
    url(r'^new$', views.newProduct), # root page or "landing" page
    url(r'^review$', views.productReview), # product review
    url(r'^/(?P<product_id>\d+)/detail$', views.producDetail), 
    url(r'^/(?P<product_id>\d+)/edit$', views.editProduct), 


    # Post or Put Routes
#    url(r'^/(?P<x>\d+)$/update', views.updateProduct),
#    url(r'^/(?P<x>\d+)$/delete', views.deleteProduct),
] 
# + static(settings.MEDIA_URL, document_root=/main/settings.MEDIA_ROOT) # will need to figure it out later. 

