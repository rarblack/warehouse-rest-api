from rest_framework import serializers

from ..models.workplace_models import WorkplaceModel


class WorkplaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkplaceModel
        fields = (
            'id', 'name', 'created_by',
            'created_datetime'
        )
