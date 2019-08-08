from . import serializers
from .models import RequestModel, DeviceModel, PartModel, WorkPlaceModel

from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from fcm_django.models import FCMDevice


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id': user.id})


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
        device.send_message(title="TEST", body="THIS IS A TEST MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        device = FCMDevice.objects.all().first()
        device.send_message(title="TEST", body="THIS IS A TEST MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
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
