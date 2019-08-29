from rest_framework import generics
from rest_framework import authentication, permissions

from fcm_django.models import FCMDevice

from ...serializers.request_serializers import RequestSerializer, RequestSerializerWithDepth
from ...models.request_models import RequestModel
from ...models.notification_models import NotificationModel


class RequestCreateApiView(generics.CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestsListApiView(generics.ListAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializerWithDepth
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestRetrieveApiView(generics.RetrieveAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializerWithDepth
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestUpdateApiView(generics.UpdateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        device = FCMDevice.objects.all().first()
        NotificationModel.objects.create(
            title='test',
            body='this is a test message',
            data='This is a test message'
        )
        device.send_message(title="TEST", body="THIS IS A TEST MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        device = FCMDevice.objects.all().first()
        NotificationModel.objects.create(
            title='test',
            body='this is a test message',
            data='This is a test message'
        )
        device.send_message(title="TEST", body="THIS IS A TEST MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
        return self.partial_update(request, *args, **kwargs)


class RequestDestroyApiView(generics.DestroyAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)