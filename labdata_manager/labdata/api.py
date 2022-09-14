from labdata.models import Labdata
from rest_framework import viewsets, permissions
from .serializers import LabdataSerializer


# CRUD Viewset
class LabdataViewSet(viewsets.ModelViewSet):
  queryset = Labdata.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LabdataSerializer