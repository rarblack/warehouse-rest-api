from rest_framework import serializers

from EquipmentPartRequestApp.models.part.models import PartModel


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartModel
        fields = (
            'id', 'name', 'created_by',
            'created_datetime'
        )