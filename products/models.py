from django.db import models


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name
    

# Product Model
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image = models.ImageField (null=True, blank=True)

    def __str__(self):
        return self.name
