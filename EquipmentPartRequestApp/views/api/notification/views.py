from rest_framework import generics
from rest_framework import authentication, permissions

from ....serializers.notification import serializers
from ....models.notification.models import NotificationModel


class NotificationsListAPIView(generics.ListAPIView):
    queryset = NotificationModel.objects.all()
    serializer_class = serializers.NotificationSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
