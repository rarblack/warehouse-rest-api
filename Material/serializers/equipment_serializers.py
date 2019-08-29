from rest_framework import serializers

from ..models import equipment_models as models


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EquipmentModel
        fields = ('id', 'name', 'sap_number', 'manufacturer', 'parts', 'work_place', 'creator', 'creation_datetime')
        depth = 1

