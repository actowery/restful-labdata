
from django.db import models

from.models import Order


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

