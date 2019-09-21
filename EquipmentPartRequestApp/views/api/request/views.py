from rest_framework import generics
from rest_framework import authentication, permissions

from fcm_django.models import FCMDevice

from ....serializers.request import serializers
from ....models.request.models import RequestModel
from ....models.notification.models import NotificationModel


class RequestTokenAuthenticatedCreateApiView(generics.CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestsTokenAuthenticatedListApiView(generics.ListAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.RequestSerializerWithDepth
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestTokenAuthenticatedRetrieveApiView(generics.RetrieveAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.RequestSerializerWithDepth
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestTokenAuthenticatedUpdateApiView(generics.UpdateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.RequestSerializer
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


class RequestTokenAuthenticatedDestroyApiView(generics.DestroyAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)