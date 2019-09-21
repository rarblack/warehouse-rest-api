from rest_framework import serializers

from EquipmentPartRequestApp.models.workplace.models import WorkplaceModel


class WorkplaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkplaceModel
        fields = (
            'id', 'name', 'created_by',
            'created_datetime'
        )
