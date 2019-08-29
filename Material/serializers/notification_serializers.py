from rest_framework import serializers

from Material.models.notification_models import NotificationModel


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationModel
        fields = ('id', 'title', 'body', 'data', 'creation_datetime')
