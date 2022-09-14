from rest_framework import serializers
from labdata.models import Labdata


class LabdataSerializer(serializers.ModelSerializer):
  class Meta:
    model = Labdata
    fields = '__all__'