from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

# Create your models here.
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# DEFINE OUR SIGNAL RECIEVER
def user_created_receiver(sender, instance, created, *args, **kwargs):
    # if USER exists, retrieve/create BillingProfile -> associate it with USER
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

# CONNECT OUR SIGNAL
# after save signal -> 'post_save'  : 
post_save.connect(user_created_receiver, sender=User)