from django.conf import settings
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from common.constants import AVAILABLE_ASSAYS

class Order(models.Model):

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
    assays = models.CharField(
        'Assay',
        choices=AVAILABLE_ASSAYS,
        max_length=10
    )
    quantity = models.PositiveIntegerField()


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

