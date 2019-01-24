import math
from django.db import models
from django.db.models.signals import pre_save, post_save

from apps.addresses.models import Address
from apps.carts.models import Cart
from apps.billing.models import BillingProfile
from main.utils import unique_order_id_generator

# ORDER STATUS OPTIONS
ORDER_STATUS_CHOICES = (
    # (stored value, Displayed value) #
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded'),
)

class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        created = False
        # QUERY for existing order
        qs = self.get_queryset().filter(billing_profile=billing_profile, cart=cart_obj, active=True, status='created')

        print("QS -> ", qs)
        
        # Found Order
        if qs.count() == 1:
            # created = False
            # variable OBJECT to assign queryset
            obj = qs.first()
            print("FOUND -> Obj -> ", obj)
        else:
            # Create object instance
            obj = self.model.objects.create(billing_profile=billing_profile, cart=cart_obj)
            created = True
            print("CREATED -> Obj -> ", obj)
        return obj, created

class Order(models.Model):
    billing_profile  = models.ForeignKey(BillingProfile, null=True, blank=True)
    shipping_address = models.ForeignKey(Address, related_name="shipping_address", null=True, blank=True)
    billing_address  = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True)
    cart             = models.ForeignKey(Cart)
    # pk / id -> unique, random
    order_id         = models.CharField(max_length=120, blank=True)
    status           = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total   = models.DecimalField(default=5.99, max_digits=7, decimal_places=2)
    total            = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    active           = models.BooleanField(default=True)

    def __str__(self):
        return self.order_id

    # attach Manager to Order
    objects = OrderManager()

    # update total instance method
    def update_total(self):
        # object variables
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        # Fixing data types -> (decimal, float)
        new_total = math.fsum([cart_total, shipping_total])
        # Format output
        formatted_total = format(new_total, '.2f')
        # Assign instance
        self.total = formatted_total
        # Save instance
        self.save()
        return new_total

    # Method to check if the ORDER is complete 
    def check_done(self):
        billing_profile = self.billing_profile
        billing_address = self.billing_address
        shipping_address = self.shipping_address
        total = self.total
        if billing_profile and billing_address and shipping_address and total > 0:
            return True
        return False

    def mark_paid(self):
        if self.check_done():
            # Update ORDER status
            self.status = "paid"
            self.save()
        return self.status
        
# GENERATE THE ORDER ID
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    # Define Queryset --> Find any existing carts
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        print("Found previous cart ... ")
        # update previous carts to be in-active
        qs.update(active=False)

# Connect Signal
pre_save.connect(pre_save_create_order_id, sender=Order)

# GENERATE THE ORDER TOTAL
def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj   = instance
        cart_total = cart_obj.total
        cart_id    = cart_obj.id
        qs         = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

# Connect Signal
post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, created, *args, **kwargs):
    print("Saving Order ...")
    if created:
        print("Updating ... Order Updated")
        instance.update_total()

# Connect Signal
post_save.connect(post_save_order, sender=Order)
