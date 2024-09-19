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
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def create_order_number(self):
        """
        Generate order number using UUID
        """
        return uuid.uuid4().hex.upper()


    def culc_total(self):
        """
        Culc grand total. accounting for deliverly cost
        """
        self.total_cost = self.lineitems.aggregate(Sum('item_total'))['item_total__sum'] or 0
        if self.total_cost > settings.FREE_DELIVERY_PRICE:
            self.deliverly_fee = settings.STANDARD_DELIVERY_PRICE
        else:
            self.deliverly_fee = 0
        self.grand_total = self.total_cost + self.deliverly_fee
        self.save()


    def save(self, *args, **kwargs):
        """
        If it has not been set, override the original save method to set the order number
        
        """
        if not self.order_number:
            self.order_number = self.create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
   



class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=True)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    
    def save(self, *args, **kwargs):
        """
        update the total cost
        
        """
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
      return f'SKU {self.product.sku} on order {self.order.order_number}'

