import re, os # regex
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.db import models

from main.utils import unique_slug_generator

# CUSTOM QUERY-SET
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)


class ProductManager(models.Manager):
    # OVERIDE normal get_queryset() method
    def get_queryset(self):
        # Use CUSTOM queryset
        return ProductQuerySet(self.model, using=self._db)

    # OVERIDE normal get all() method
    def all(self):
        # retrieve only "active" querysets
        return self.get_queryset().active()

    def featured(self):  # Product.objects.featured()
        # retrieve only "featured" querysets
        return self.get_queryset().featured()

    def get_by_id(self, id):
        # Product.objects == self.get_queryset()
        qs = self.get_queryset().filter(id=id)  # Load qs into variable
        # only found 1 -> ?
        if qs.count() == 1:
            return qs.first()
        # nothing found
        return None

class Product(models.Model):
    name            = models.CharField(max_length=120)
    description     = models.TextField()
    slug			= models.SlugField(blank=True, unique=True)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    thumb           = models.ImageField(default='default.svg.png', blank=True)
    # color           = models.CharField(max_length=120)
    # size            = models.CharField(max_length=120)
    # category        = models.CharField(max_length=120)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Associate ModelManager()
    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    # could also be done like this
    def __repr__(self):
        return "<User {} | {} | {}>".format(self.id, self.name, self.description)

    def __str__(self):
        info = str(self.id) + " " + self.name + " " + str(self.price)
        return info


# SIGNALS -> PRE_SAVE
def product_presave_reciever(sender, instance, *args, **kwargs):
    # if not already created -> create it
    if not instance.slug:
        # generate a unique slug name
        instance.slug = unique_slug_generator(instance)

# ATTACH SIGNAL
pre_save.connect(product_presave_reciever, sender=Product)


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
