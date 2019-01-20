from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from apps.product.models import Product

# USE BUILT IN DJANGO USER MODEL
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):

    def new_or_get(self, request):
        # retrieve cart ID or object=None
        cart_id = request.session.get("cart_id", None)
        # filter queryset with found cart_id
        qs = self.get_queryset().filter(id=cart_id)
        # Found query
        if qs.count() == 1:
            # Initalize obj variable
            new_obj = False
            # Initalize cart object
            cart_obj = qs.first()
            # Associate logged in user with cart
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            # Create a new cart with logged in user association
            cart_obj = Cart.objects.new(user=request.user)
            # Initalize obj variable
            new_obj = True
            # Load cart_id in session context
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        # initalize obj variable -> User object
        user_obj = None
        # User exists -> (?)
        if user is not None:
            # logged in -> (?)
            if user.is_authenticated():
                # assign user object
                user_obj = user
        return self.model.objects.create(user=user_obj)


# Create your models here.
class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Attach CartManager()
    objects = CartManager()

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "<Cart object: {}: {}>".format(self.id, self.total)


# CALLED WHENEVER WE HIT SAVE
def m2m_changed_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        # QUERYSET
        products = instance.products.all()
        # Initalize calculation variable -> 'total'
        total = 0
        # Loop through products
        for item in products:
            # find total 
            total += item.price
            print("ITEM: ", item)
        if instance.subtotal != total:
            # assign -> 'subtotal'
            instance.subtotal = total
            instance.save()
        print("Total: ", total)

# Connect signal
m2m_changed.connect(m2m_changed_cart_reciever, sender=Cart.products.through)

def pre_save_cart_reciever(sender, instance, *args, **kwargs):
    # Subtotal exists -> (?) 
    if instance.subtotal > 0:
        # Calculate Sales Tax
        instance.total = Decimal(instance.subtotal) * Decimal(1.08)  # -> add 8% Tax
    else:
        # Assign Zero Dollars -> 'total'
        instance.total = 0.00

# Connect signal
pre_save.connect(pre_save_cart_reciever, sender=Cart)
