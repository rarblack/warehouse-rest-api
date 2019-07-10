from rest_framework import serializers
from .models import RequestModel, WorkPlaceModel, PartModel


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = ('img_url', 'parts', 'work_place', 'sap_number', 'manufacturer', 'quantity', 'size', 'weight', 'comment', 'status', 'creator', 'creation_datetime')


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartModel
        fields = ('name', 'creator', 'creation_datetime')


class WorkPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkPlaceModel
        fields = ('name', 'creator', 'creation_datetime')
