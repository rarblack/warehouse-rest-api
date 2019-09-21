from rest_framework import generics
from rest_framework import authentication, permissions

from ....serializers.workplace import serializers
from ....models.workplace.models import WorkplaceModel


class WorkplacesListCreate(generics.ListCreateAPIView):
    queryset = WorkplaceModel.objects.all()
    serializer_class = serializers.WorkplaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class WorkplaceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkplaceModel.objects.all()
    serializer_class = serializers.WorkplaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
