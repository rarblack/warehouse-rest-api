from rest_framework import serializers

from EquipmentPartRequestApp.models.equipment import models as models


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EquipmentModel
        fields = (
            'id', 'name', 'sap',
            'manufacturer', 'parts', 'workplace',
            'created_by', 'created_datetime'
        )
        depth = 1

