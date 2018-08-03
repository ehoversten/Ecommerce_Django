from django.db import models
import math
import datetime
from django.conf import settings
from django.db import models
from django.db.models import Count, Sum, Avg
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils import timezone

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
    order_id            = models.CharField(max_length=120, blank=True) # AB31DE3
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_id

    objects = OrderManager()

    class Meta:
       ordering = ['-timestamp', '-updated']

    def get_absolute_url(self):
        return reverse("orders:detail", kwargs={'order_id': self.order_id})

    def get_status(self):
        if self.status == "refunded":
            return "Refunded order"
        elif self.status == "shipped":
            return "Shipped"
        return "Shipping Soon"

#Order detail

class OrderDetail(models.Model):
    order_detail_id   = models.CharField(max_length=120, blank=True) # AB31DE3
    quantity          = models.IntegerField(max_length=100, blank=True) 
    comments          = models.CharField(max_length=1000)
    updated_at        = models.DateTimeField(auto_now=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    order_id          = models.ForeignKey(Order)

    def __str__(self):
        return self.order_detail_id

    # active              = models.BooleanField(default=True)
    # shipping_address    = models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True)
    # billing_address     = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True)
    # shipping_address_final    = models.TextField(blank=True, null=True)
    # billing_address_final     = models.TextField(blank=True, null=True)


# ADDRESS_TYPES = (
#     ('billing', 'Billing address'),
#     ('shipping', 'Shipping address'),
# )

#Adress model
# class Address(models.Model):
#     billing_profile = models.ForeignKey(BillingProfile)
#     name            = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
#     nickname        = models.CharField(max_length=120, null=True, blank=True, help_text='Internal Reference Nickname')
#     address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
#     address_line_1  = models.CharField(max_length=120)
#     address_line_2  = models.CharField(max_length=120, null=True, blank=True)
#     city            = models.CharField(max_length=120)
#     country         = models.CharField(max_length=120, default='U S of A')
#     state           = models.CharField(max_length=120)
#     postal_code     = models.CharField(max_length=120)

#     def __str__(self):
#         if self.nickname:
#             return str(self.nickname)
#         return str(self.address_line_1)

#     def get_absolute_url(self):
#         return reverse("address-update", kwargs={"pk": self.pk})

#     def get_short_address(self):
#         for_name = self.name 
#         if self.nickname:
#             for_name = "{} | {},".format( self.nickname, for_name)
#         return "{for_name} {line1}, {city}".format(
#                 for_name = for_name or "",
#                 line1 = self.address_line_1,
#                 city = self.city
#             ) 

#     def get_address(self):
#         return "{for_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
#                 for_name = self.name or "",
#                 line1 = self.address_line_1,
#                 line2 = self.address_line_2 or "",
#                 city = self.city,
#                 state = self.state,
#                 postal= self.postal_code,
#                 country = self.country
#             )
