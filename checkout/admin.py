from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrdertotalAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrdertotalAdmin,)

    readonly_fields = ('order_number', 'date', 'deliverly_fee', 
                       'total_cost', 'grand_total', 'original_bag', 'stripe_pid')
    
    fields = ('order_number', 'user_profile', 'date', 
              'full_name', 'phone', 'eircode', 'country', 
              'address1', 'address2', 'town_city', 'county_region', 
              'deliverly_fee','total_cost','grand_total','original_bag','stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'total_cost', 'deliverly_fee', 'grand_total')

    ordering = ('-date', )


admin.site.register(Order,OrderAdmin)