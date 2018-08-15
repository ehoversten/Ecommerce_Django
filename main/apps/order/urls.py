from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views


urlpatterns = [
      # URL pattern for the order
    # Get routes
    url(r'^$', views.library), # root page or "library" page
    url(r'^view_order$', views.order_detail), # root page or order details
    url(r'^view_list$', views.order_list), # order list
    
]