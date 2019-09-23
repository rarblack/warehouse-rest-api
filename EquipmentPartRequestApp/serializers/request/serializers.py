from rest_framework import serializers

from EquipmentPartRequestApp.models.request.models import RequestModel


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = (
            'id', 'image', 'equipment', 'parts',
            'quantity', 'size', 'weight', 'comment',
            'status', 'created_by', 'created_datetime'
        )


class RequestSerializerWithDepth(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = (
            'id', 'image', 'equipment', 'parts',
            'quantity', 'size', 'weight', 'comment',
            'status', 'created_by', 'created_datetime'
        )
        depth = 1
