from rest_framework import serializers

from ..models.notification_models import NotificationModel


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationModel
        fields = ('id', 'title', 'body', 'data', 'creation_datetime')
