from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'News: {self.title}'

