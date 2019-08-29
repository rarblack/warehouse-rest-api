from rest_framework import serializers

from Material.models.part_models import PartModel


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartModel
        fields = ('id', 'name', 'creator', 'creation_datetime')