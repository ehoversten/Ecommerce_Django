from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from apps.product.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.exists() and qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new_cart(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


# Create your models here.
class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "<Cart object: {}: {}>".format(self.id, self.total)


# CALLED WHENEVER WE HIT SAVE
def m2m_changed_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        print(action)
        products = instance.products.all()
        total = 0
        for item in products:
            total += item.price
            print("ITEM: ", item)
            instance.subtotal = total
            instance.save()
        print("Total: ", total)


m2m_changed.connect(m2m_changed_cart_reciever, sender=Cart.products.through)

def pre_save_cart_reciever(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal + 10

pre_save.connect(pre_save_cart_reciever, sender=Cart)
