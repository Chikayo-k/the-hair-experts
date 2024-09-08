import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product


# Create your models here.

class Order(models.Model):

    order_number = models.CharField(max_length=30, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    eircode = models.CharField(max_length=15,null=True, blank=True )
    country = models.CharField(max_length=40, null=False, blank=False)
    address1 = models.CharField(max_length=50,null=False, blank=False)
    address2 = models.CharField(max_length=50,null=True, blank=True)
    town_city = models.CharField(max_length=50,null=False, blank=False)
    county_region = models.CharField(max_length=50,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    deliverly_fee = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=0)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
   



class OrderItem(models.model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=True)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

