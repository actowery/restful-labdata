from django.contrib import admin
from .models import Order, OrderAssay
from .forms import OrderAssayForm, OrderAssayFormSet

class OrderAssayInline(admin.TabularInline):
    model = OrderAssay

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'created_at',
        'updated_at',
        'company',
        'display_order_assays',
    ]
    inlines = [
        OrderAssayInline,
    ]

    def order_number(self, obj):
        return obj.order_number()

    def get_formsets(self, request, obj=None):
        # Use the custom formset for OrderAssay
        formsets = super().get_formsets(request, obj=obj)
        if obj is None:
            # Create formsets
            for formset in formsets:
                if issubclass(formset.form, OrderAssayForm):
                    formset.form = OrderAssayFormSet
        return formsets

    def display_order_assays(self, obj):
        order_assays = OrderAssay.objects.filter(order=obj)
        return ', '.join([str(order_assay) for order_assay in order_assays])

    display_order_assays.short_description = 'Order Assays'

admin.site.register(Order, OrderAdmin)