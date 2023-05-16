from django.conf import settings
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from common.constants import AVAILABLE_ASSAYS, STATUS_OPTIONS, RESTULT_OPTIONS

import datetime
import uuid



class Order(models.Model):

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    
    def default_order():
        return ()
        
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.RESTRICT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.TextField()



class OrderAssay(models.Model):
    class Meta:
        verbose_name = "Assay Batch"
        verbose_name_plural = "Assay Batches"
        unique_together = ('order', 'assay')

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.PositiveIntegerField(default=1)
    assay = models.CharField(max_length=5, choices=AVAILABLE_ASSAYS)

    @staticmethod
    def get_default_order_assay():
        default_order_assay, _ = OrderAssay.objects.get_or_create(
            # Specify the default values for the OrderAssay fields
            # For example:
            assay="Default Assay",
            quantity=1
        )
        return default_order_assay
    

class Assay(models.Model):

    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = 'Other Assay See Order Comment'
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default='P')
    result = models.CharField(max_length=1, choices=RESTULT_OPTIONS, default='I')
    order_assay = models.ForeignKey(OrderAssay, on_delete=models.CASCADE, related_name='assay_batches',\
                                default=OrderAssay.get_default_order_assay)   
    def __str__(self):
        # Zebra-printer conscious naming convention TEST_DATE_ID (truncate to 8 chars)
        # e.g. PCR_2022_01_01_47e4f259
        return f"{self.name}_{datetime.datetime.now().strftime('%Y_%m_%d')}_{str(self.id)[:8]}"



class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("order_list")



