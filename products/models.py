from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


# Product Model
class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# Reviews for products
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='chosen_product') # noqa  
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='commenter')
    review_title = models.CharField(max_length=20)
    comment_area = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return f'Comment for : {self.product}'
