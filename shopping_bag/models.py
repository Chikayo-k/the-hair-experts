from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
   user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user')
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
   date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
     return f"{self.user}'s wish list "
