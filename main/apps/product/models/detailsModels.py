import re
from datetime import datetime

from productModels import Product
from django.db import models

""" Missing the validator, will have to figure out logic on how to implement them when creating a product to pass the color, size, and category with it. -Jose 8/4 """

class Color(models.Model):
    name            = models.CharField(max_length=120)

    """ Since it is 'Product' can have many colors, we only need the ForeignKey """
    # Foreign key
    pColor         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    # objects = colorValidator() ## Not sure if we are gonna need this.
    def __str__(self):
        
        return self.name 


class Size(models.Model):
    name            = models.CharField(max_length=120)

    # Foreign key
    pSize         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    # objects = SizeValidator() ## Not sure if we are gonna need this.
    def __str__(self):
        return self.name 


class Category(models.Model):
    name            = models.CharField(max_length=120)

    # Foreign key
    product         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    # objects = CategoryValidator() ## Not sure if we are gonna need this.
    def __str__(self):
        return self.name 
