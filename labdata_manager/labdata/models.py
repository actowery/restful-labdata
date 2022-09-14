from django.db import models

# Create your models here.
class Labdata(models.Model):
  test_id = models.UUIDField(unique=True)
  result_type = models.CharField(max_length=100)
  value = models.IntegerField()
  note = models.CharField(max_length=500, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)