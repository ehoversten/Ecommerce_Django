from django.contrib import admin
from ..product.models import (Size, Category, Color, Product)


admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)

