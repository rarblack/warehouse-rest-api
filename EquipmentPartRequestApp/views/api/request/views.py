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


class RequestTokenAuthenticatedDestroyApiView(generics.DestroyAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
