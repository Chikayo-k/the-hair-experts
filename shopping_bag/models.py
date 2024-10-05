from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Recommendation(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
   recommendation_title = models.CharField(max_length=30)
   description = models.TextField()
   exclusive = models.CharField(max_length=30)
   
   def __str__(self):
     return f"Recommendation for {self.product}"
