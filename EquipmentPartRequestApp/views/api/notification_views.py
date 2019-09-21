from rest_framework import generics
from rest_framework import authentication, permissions

from ...serializers.notification_serializers import NotificationSerializer
from ...models.notification_models import NotificationModel


class NotificationsListAPIView(generics.ListAPIView):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
