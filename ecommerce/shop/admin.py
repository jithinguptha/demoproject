from django.contrib import admin

from shop.models import category

from shop.models import product

# Register your models here.
admin.site.register(category)
admin.site.register(product)