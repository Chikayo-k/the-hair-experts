from django.contrib import admin
from .models import Product, Category

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'image',
    )

    ordering = ('sku',)


class AdminCategory(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)