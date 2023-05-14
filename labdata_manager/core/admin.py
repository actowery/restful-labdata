from django.contrib import admin
from .models.models import Order
from .models.assays import Assay

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'updated_at',
        'company',
        'display_assays',
    ]

    def display_assays(self, obj):
        return ', '.join([assay.name for assay in obj.assays.all()])
 
    display_assays.short_description = 'Assays'
admin.site.register(Order, OrderAdmin)

