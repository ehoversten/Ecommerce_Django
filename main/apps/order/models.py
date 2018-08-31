from django.db import models
import math
import datetime
from django.conf import settings
from django.db import models
from django.db.models import Count, Sum, Avg
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils import timezone
# from ..product.models.productModels import Product
# from ..product.models.detailsModels import Color, Size, Category
from ..loginRegistration.models import User

# for future feature 
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

#OrderManager
class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        created = False
        qs = self.get_queryset().filter(
                billing_profile=billing_profile,  
                active=True, 
                status='created'
            )
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(
                    billing_profile=billing_profile, 
                    cart=cart_obj)
            created = True
        return obj, created

#Order Model
class Order(models.Model):
    order_by            = models.ForeignKey(User, related_name="user_order")
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=5.99, max_digits=65, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=65, decimal_places=2)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_by

    objects = OrderManager()

    class Meta:
       ordering = ['-timestamp', '-updated']

    def get_absolute_url(self):
        return reverse("orders:detail", kwargs={'order_id': self.order_by})

    def get_status(self):
        if self.status == "refunded":
            return "Refunded order"
        elif self.status == "shipped":
            return "Shipped"
        return "Shipping Soon"

#Order detail

class OrderDetail(models.Model):
    order_detail_id   = models.CharField(max_length=120, blank=True) # AB31DE3
    quantity          = models.IntegerField()
    price             = models.DecimalField(max_digits= 10, decimal_places=2) 
    comments          = models.CharField(max_length=1000)
    updated_at        = models.DateTimeField(auto_now=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    # item              = models.ForeignKey(Product, related_name ='orderitem')
    # def __str__(self):
    #     return self.item.name

   