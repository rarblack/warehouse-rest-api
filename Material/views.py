from rest_framework import generics
from rest_framework import authentication, permissions
from . import serializers
from fcm_django.models import FCMDevice

from .models import RequestModel, DeviceModel, PartModel, WorkPlaceModel


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.CreateUpdateDestroyRequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestsListAPIView(generics.ListAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.ListRetrieveRequestsSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestRetrieveAPIView(generics.RetrieveAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.ListRetrieveRequestsSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestUpdateAPIView(generics.UpdateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.CreateUpdateDestroyRequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        device = FCMDevice.objects.all().first()
        device.send_message(data={"test": "test"})
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        device = FCMDevice.objects.all().first()
        device.send_message(data={"test": "test"})
        return self.partial_update(request, *args, **kwargs)


class RequestDestroyAPIView(generics.DestroyAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = serializers.CreateUpdateDestroyRequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RetrieveDevice(generics.RetrieveAPIView):
    queryset = DeviceModel.objects.all()
    serializer_class = serializers.DeviceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class CreateListParts(generics.ListCreateAPIView):
    queryset = PartModel.objects.all()
    serializer_class = serializers.PartSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class PartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartModel.objects.all()
    serializer_class = serializers.PartSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class CreateListWorkPlaces(generics.ListCreateAPIView):
    queryset = WorkPlaceModel.objects.all()
    serializer_class = serializers.WorkPlaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class WorkPlaceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkPlaceModel.objects.all()
    serializer_class = serializers.WorkPlaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
