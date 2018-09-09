import re  # regex
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# product details
class Category(models.Model):
    name            = models.CharField(max_length=120)
    # pCategory = models.ManyToManyField(Product,related_name="cTproduct_id")

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Color(models.Model):
    name            = models.CharField(max_length=120)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Size(models.Model):
    name            = models.CharField(max_length=120)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

# class Image(models.Model):
#     thumb = models.ImageField(default='default.svg.png', blank=True)
#     created_at      = models.DateTimeField(auto_now_add=True)
#     updated_at      = models.DateTimeField(auto_now_add=True)
#     timestamp       = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.name


# Product 

class Product(models.Model):
    name            = models.CharField(max_length=120)
    brand           = models.CharField(max_length=120) # this will put on the product details later
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    inStock         = models.BooleanField(default=True)
    quantity        = models.IntegerField(default=1)
    quantitySold = models.IntegerField(default=0)
    thumb = models.ImageField(default='default.svg.png', blank=True)
    # Not sure how to do implement this one.
    # image            = models.ManyToManyField(Image, related_name="image_id")
    ## Foreign keys.
    seller          = models.ForeignKey(User, related_name="user_id",null=True, blank=True)
    
    category        = models.ManyToManyField(Category,related_name="category_id")
    color           = models.ManyToManyField(Color, related_name="color_id")
    size            = models.ManyToManyField(Size, related_name="size_id")


    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    # could also be done like this
    # def __repr__(self):
    #     return "<User {} | {} | {}>".format(self.id, self.name, self.description)
    def __str__(self):
        info = self.name + " " + str(self.price)
        return info
