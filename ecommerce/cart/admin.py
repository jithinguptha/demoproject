from django.contrib import admin

from cart.models import cart

from cart.models import order, account

# Register your models here.
admin.site.register(cart)
admin.site.register(order)
admin.site.register(account)
