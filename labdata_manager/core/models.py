from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser

from pathlib import Path
import json
import ast


class Order(models.Model):

    def __str__(self):
        return str(self.pk)

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
    assays = models.ManyToManyField(
        'Assay',
        related_name='orders'
    )


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


class Assay(models.Model):
    STATUS_OPTIONS = [
        ('P', 'Pending'),
        ('R', 'Running'),
        ('C', 'Complete'),
    ]

    RESTULT_OPTIONS = [
        ('P', 'Pass'),
        ('F', 'Fail'),
        ('I', 'Incomplete'),
        ('E', 'Error'),
    ]

    name = 'Other Assay See Order Comment'
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default='P')
    result = models.CharField(max_length=1, choices=RESTULT_OPTIONS, default='I')
    
class PCR(Assay):
    name = 'PCR'

class ELISA(Assay):
    name = 'ELISA'


with open(str(Path(__file__).absolute()), 'r') as file:
    contents = file.read()
    p = ast.parse(contents)

    classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
    print(classes)