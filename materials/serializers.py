from rest_framework import serializers
from . import models


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MaterialsModel
        fields = ('user', 'file', 'order', 'parts', 'quantity')