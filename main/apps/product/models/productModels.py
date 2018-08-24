import re  # regex
from datetime import datetime

from django.db import models

from ...product.models.detailsModels import Color, Size, Category
from ...product.models.detailsModels import ColorManager ## This is how we can use the colormanager


from ...loginRegistration.models import User

""" I've abstracted the details for the product to 'detailsModels' this will keep it a little neater hopefully -Jose 8/4 """

class ProductManager(models.Manager):

    def ProductManager(self, form, user_id):
        errors = []

        if not form['name']:
            errors.append('Product name is required.')
        if len(form['name']) < 3:
            errors.append('Product name needs to be more than 3 characters.')
        if not form['brand']:
            errors.append('Brand name is required.')
        if len(form['brand']) < 2:
            errors.append('Brand name needs to be more than 2 characters.')
        if not form['description']:
            errors.append('Product description can\'t be empty.')
        if len(form['description']) < 3:
            errors.append('Product description needs to be more than 3 characters.')
        if not form['price']:
            errors.append('Please provide a price for the product.')

        if not errors:
            seller = User.objects.get(id=user_id)
            product = Product.objects.create(product=form['product'], seller=seller)
            return (True, product)
        else:
            return (False, errors)

    


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
    """ blank=True determines whether the field will be required in forms. This includes the admin and your own custom forms. If blank=True then the field will not be required, whereas if it's False the field cannot be blank """
    # order          = models.OneToManyField(Review, related_name="product_id",null=True, blank=True)
    
    # review          = models.OneToManyField(Review, related_name="product_id",null=True, blank=True)
    # size          = models.OneToManyField(Review, related_name="product_id",null=True, blank=True)
    # color          = models.OneToManyField(Review, related_name="product_id",null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()
    # could also be done like this 
    # def __repr__(self):
    #     return "<User {} | {} | {}>".format(self.id, self.name, self.description)
    def __str__(self):
        info = self.name + " " + self.price
        return info
