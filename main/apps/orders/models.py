from django.db import models

from apps.carts.models import Cart

ORDER_STATUS_CHOICES = (
    # (stored value, Displayed value) #
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded'),
)

# Create your models here.

class Order(models.Model):
    # pk / id
    order_id = models.CharField(max_length=120, blank=True)
    # billing_profile
    # shipping_address
    # billing_address
    carts          = models.ForeignKey(Cart)
    status         = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=7, decimal_places=2)
    order_total    = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.order_id



    # GENERATE THE ORDER ID
    # GENERATE THE ORDER TOTAL