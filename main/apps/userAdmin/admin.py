from django.contrib import admin
from ..product.models.productModels import Product
from ..product.models.detailsModels import (Size,Category, Color)


admin.site.register(Product)
