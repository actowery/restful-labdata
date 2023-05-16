from django.contrib import admin
from .models import Order, OrderAssay

class OrderAssayInline(admin.TabularInline):
    model = OrderAssay

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'updated_at',
        'company',
        'display_order_assays',
    ]
    inlines = [
        OrderAssayInline,
    ]

    def display_order_assays(self, obj):
        order_assays = OrderAssay.objects.filter(order=obj)
        return ', '.join([order_assay.name for order_assay in order_assays])

    display_order_assays.short_description = 'Order Assays'

admin.site.register(Order, OrderAdmin)