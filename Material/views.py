from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import RequestSerializer, DeviceSerializer, PartSerializer, WorkPlaceSerializer
from .models import RequestModel, DeviceModel, PartModel, WorkPlaceModel


class CreateListRequests(generics.ListCreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RetrieveDevice(generics.RetrieveAPIView):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class RequestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class CreateListParts(generics.ListCreateAPIView):
    queryset = PartModel.objects.all()
    serializer_class = PartSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class PartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartModel.objects.all()
    serializer_class = PartSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class CreateListWorkPlaces(generics.ListCreateAPIView):
    queryset = WorkPlaceModel.objects.all()
    serializer_class = WorkPlaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class WorkPlaceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkPlaceModel.objects.all()
    serializer_class = WorkPlaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)