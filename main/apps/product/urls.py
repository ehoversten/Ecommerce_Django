from django.conf.urls import url
from . import views
from .views import ProductListView, ProductDetailSlugView

app_name = 'Product'

# Get routes
urlpatterns = [
    # root page or "landing" page
    url(r'^$',ProductListView.as_view(), name ='landing'),
    # instead of using product id we render product by its slug number
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name="detail"),
    # url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    # url(r'^(?P<product_id>\d+)/productDetail$', views.productDetail),
    url(r'^new$', views.product_new, name='new' ),
    url(r'^review$', views.product_review, name='review'), # product review
    url(r'^(?P<product_id>\d+)/edit$', views.editProduct),
    # Post or Put Routes
#    url(r'^/(?P<x>\d+)$/update', views.updateProduct),
#    url(r'^/(?P<x>\d+)$/delete', views.deleteProduct),
]
# + static(settings.MEDIA_URL, document_root=/main/settings.MEDIA_ROOT) # will need to figure it out later.
