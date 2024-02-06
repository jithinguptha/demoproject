from django.contrib.auth.models import User
from django.db import models

from django.db.models import ForeignKey
from shop.models import product

from django.http import HttpResponse


# Create your models here.
class cart(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.quantity * self.product.price


class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    address = models.TextField()
    phone = models.IntegerField()
    order_status = models.CharField(default="pending",max_length=20)
    delivery_status = models.CharField(default="pending",max_length=20)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class account(models.Model):
    accountnum = models.CharField(max_length=20)
    accounttype = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return self.accountnum
