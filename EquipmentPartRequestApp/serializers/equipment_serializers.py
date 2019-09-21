from rest_framework import serializers

from ..models import equipment_models as models


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EquipmentModel
        fields = (
            'id', 'name', 'sap_number',
            'manufacturer', 'parts', 'workplace',
            'created_by', 'created_datetime'
        )
        depth = 1

