from rest_framework import generics
from rest_framework import authentication, permissions

from ...serializers.part_serializers import PartSerializer
from ...models.part_models import PartModel


class PartsListCreateApiView(generics.ListCreateAPIView):
    queryset = PartModel.objects.all()
    serializer_class = PartSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class PartRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartModel.objects.all()
    serializer_class = PartSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
