from rest_framework import serializers

from Material.models.request_models import RequestModel


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = ('id', 'image', 'parts', 'work_place', 'sap_number', 'manufacturer', 'quantity', 'size', 'weight', 'comment', 'status', 'creator', 'creation_datetime')


class RequestSerializerWithDepth(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = ('id', 'image', 'parts', 'work_place', 'sap_number', 'manufacturer', 'quantity', 'size', 'weight', 'comment', 'status', 'creator', 'creation_datetime')
        depth = 1
