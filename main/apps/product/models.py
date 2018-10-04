import re, os # regex
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.db import models


""" # product details
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
 """
class Product(models.Model):
    name           = models.CharField(max_length=120)
    description     = models.TextField()
    slug			= models.SlugField(blank=True, unique=True)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    thumb = models.ImageField(default='default.svg.png', blank=True)
    color           = models.CharField(max_length=120)
    size            = models.CharField(max_length=120)
    category        = models.CharField(max_length=120)


    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    # could also be done like this
    # def __repr__(self):
    #     return "<User {} | {} | {}>".format(self.id, self.name, self.description)
    def __str__(self):
        info = self.name + " " + str(self.price)
        return info
