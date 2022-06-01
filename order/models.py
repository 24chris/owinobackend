from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    notes = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    #other fields for order
    # paid_amount = models.IntegerField(blank=True,null=True)
    # flutterwave_token = models.CharField(max_length=100)


    class Meta:
        ordering = ['-created_at',]

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s'%self.id

