from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from apps.accounts.models import GuestEmail

# Django provided AUTHORIZED USER
User = settings.AUTH_USER_MODEL

class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        # grab the user
        user = request.user
        # Load into --> session
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj = None
        if user.is_authenticated():
            # 'logged in user checkout; remember payment stuff'
            # Get or Initalize a Billing Profile with current user and email
            obj, created = self.model.objects.get_or_create(
                user=user, email=user.email)
        elif guest_email_id is not None:
            # 'guest user checkout; auto reloads payment stuff'
            # Grab the guest ID
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            # Get or Initalize a Billing Profile with guest user and guest email
            obj, created = self.model.objects.get_or_create(
                email=guest_email_obj.email) # self.model.objects -> BillingProfile.objects
        else:
            pass
        return obj, created

# Create your models here.
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    objects = BillingProfileManager()       

    def __str__(self):
        return self.email

# DEFINE OUR SIGNAL RECIEVER
# See DOCS -> https://docs.djangoproject.com/en/1.10/topics/signals/
def user_created_receiver(sender, instance, created, *args, **kwargs):
    # if USER exists, retrieve/create BillingProfile -> associate it with USER
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

# CONNECT OUR SIGNAL
# after save signal -> 'post_save'  : 
post_save.connect(user_created_receiver, sender=User)
