from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Order(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.RESTRICT,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})