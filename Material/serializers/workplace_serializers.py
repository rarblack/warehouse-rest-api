from rest_framework import serializers

from Material.models.workplace_models import WorkplaceModel


class WorkplaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkplaceModel
        fields = ('id', 'name', 'creator', 'creation_datetime')
