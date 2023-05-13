
from django.db import models
from django.urls import reverse

from.models import Order
from pathlib import Path
import ast

def assay_list():
    classes = []
    with open(str(Path(__file__).absolute()), 'r') as file:
        contents = file.read()
        p = ast.parse(contents)

        classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
    return classes

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

