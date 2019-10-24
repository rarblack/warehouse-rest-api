from rest_framework import serializers

from EquipmentPartRequestApp.models.notification.models import NotificationModel


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationModel
        fields = (
            'id', 'title', 'created_datetime'
        )
