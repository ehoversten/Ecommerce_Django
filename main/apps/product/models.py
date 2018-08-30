import re  # regex
from datetime import datetime

from django.db import models
# from ..loginRegistration.models import User
from django.contrib.auth.models import User


class Category(models.Model):
    name            = models.CharField(max_length=120)
    # pCategory = models.ManyToManyField(Product,related_name="cTproduct_id")

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 

class Product(models.Model):
    name            = models.CharField(max_length=120)
    brand           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    inStock         = models.BooleanField(default=True)
    quantity        = models.IntegerField(default=1)
    quantitySold    = models.IntegerField(default=0)
    # image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True) # Not sure how to do implement this one.

    ## Foreign keys. 
    seller         = models.ForeignKey(User, related_name="user_id",null=True, blank=True)
    pCategory      = models.ManyToManyField(Category,related_name="cCategory_id")

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    # could also be done like this 
    # def __repr__(self):
    #     return "<User {} | {} | {}>".format(self.id, self.name, self.description)
    def __str__(self):
        info = self.name + " " + str(self.price)
        return info


# Product Details

class Color(models.Model):
    name            = models.CharField(max_length=120)
    pColor          = models.ManyToManyField(Product,related_name="cProduct_id")

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 


class Size(models.Model):
    name            = models.CharField(max_length=120)
    pSize           = models.ManyToManyField(Product, related_name="sProduct_id")

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


# class Category(models.Model):
#     name            = models.CharField(max_length=120)
#     # pCategory = models.ManyToManyField(Product,related_name="cTproduct_id")

#     created_at      = models.DateTimeField(auto_now_add=True)
#     updated_at      = models.DateTimeField(auto_now_add=True)
#     timestamp       = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.name 