from django.db import models

from apps.billing.models import BillingProfile

# declare tuple for selecting billing or shipping address
ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

# Create your models here.
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_1       = models.CharField(max_length=120)
    address_2       = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    state           = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='United States')
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)