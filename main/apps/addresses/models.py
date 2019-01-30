from django.db import models

from apps.billing.models import BillingProfile

# declare tuple for selecting billing or shipping address
ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)

# Create your models here.
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    state           = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='United States')
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{city}\n, {state}{postal}\n{country}\n".format(line1=self.address_line_1, line2=self.address_line_2, city=self.city, state=self.state, country=self.country, postal=self.postal_code)
