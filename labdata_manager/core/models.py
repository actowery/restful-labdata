from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import CustomUser
import json

class Order(models.Model):

    def __str__(self):
        return f"{self.user.username}'s order for {self.quantity} {self.item}(s) totaling ${self.total_cost}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    
    def default_order():
        default_json = {"test1": {"num_tests": 0,"lot_numbers": []},\
            "test2": {"num_tests": 0,"lot_numbers": []},\
            "test3": {"num_tests": 0,"lot_numbers": []}}
        return default_json
    
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.RESTRICT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.TextField()
    assays = models.JSONField(default=default_order())