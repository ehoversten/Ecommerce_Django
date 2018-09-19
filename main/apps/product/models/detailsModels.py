import re
from datetime import datetime

from django.db import models
# from ...product.models.productModels import Product

"""I tried implementing the ColorManager on the productModels but it doesnt seem to like that.
Will have to implement it a different way, maybe create the product and send it to the details models after that. We could also create and 'instance' of the class in the Product Models -Jose 8/15 """




class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    slug			= models.SlugField(blank=True, unique=True)
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    color           = models.CharField(max_length=120)
    size            = models.IntegerField(max_length=120)
    category        = models.CharField(max_length=120)

class ColorManager(models.Manager):
    def ColorManager(self, form, product_id ):
        errors = []

        if not form['name']:
            errors.append('Color name is required for the product.')
        if len(form['name']) < 3:
            errors.append('Product name needs to be more than 3 characters.')

class SizeManager(models.Manager):
    def SizeManager(self, form, product_id ):
        errors = []

        if not form['size']:
            errors.append('Size name is required for the product.')
        if len(form['size']) < 2:
            errors.append('size name needs to be more than 1 character.')

class CategoryManager(models.Manager):
    def CategoryManager(self, form, product_id ):
        errors = []

        if not form['category']:
            errors.append('Category name is required for the product.')
        if len(form['category']) < 2:
            errors.append('Category name needs to be more than 2 characters.')
    
# class BrandManager(models.Manager):
#     def BrandManager(self, form, product_id ):
#         errors = []

#         if not form['category']:
#             errors.append('Category name is required for the product.')
#         if len(form['category']) < 2:
#             errors.append('Category name needs to be more than 2 characters.')
    


class Color(models.Model):
    name            = models.CharField(max_length=120)

    """ Since it is 'Product' can have many colors, we only need the ForeignKey """
    # Foreign key
    # pColor         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    objects = ColorManager()

    # objects = colorValidator() ## Not sure if we are gonna need this.
    def __str__(self):
        
        return self.name 


class Size(models.Model):
    name            = models.CharField(max_length=120)

    # Foreign key
    # pSize         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    objects = SizeManager()

    # objects = SizeValidator() ## Not sure if we are gonna need this.
    def __str__(self):
        return self.name 


class Category(models.Model):
    name            = models.CharField(max_length=120)

    # Foreign key
    # pCategory         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    objects = CategoryManager()

# class Brand(models.Model):
#     name            = models.CharField(max_length=120)

#     # Foreign key
#     pBrand         = models.ForeignKey(Product, related_name="product_id",null=True, blank=True)

#     created_at      = models.DateTimeField(auto_now_add=True)
#     updated_at      = models.DateTimeField(auto_now_add=True)
#     timestamp       = models.DateTimeField(auto_now_add=True)
#     objects = BrandManager()


    # objects = CategoryValidator() ## Not sure if we are gonna need this.
    def __str__(self):
        return self.name 
