from rest_framework import serializers
from .models import RequestModel, WorkPlaceModel, DeviceModel, PartModel


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = ('id','img_url', 'parts', 'work_place', 'sap_number', 'manufacturer', 'quantity', 'size', 'weight', 'comment', 'status', 'creator', 'creation_datetime')


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceModel
        fields = ('id', 'name', 'sap_number', 'manufacturer', 'parts', 'work_place', 'creator', 'creation_datetime')


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartModel
        fields = ('id', 'name', 'creator', 'creation_datetime')


class WorkPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkPlaceModel
        fields = ('id', 'name', 'creator', 'creation_datetime')
