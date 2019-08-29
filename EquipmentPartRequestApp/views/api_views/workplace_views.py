from rest_framework import generics
from rest_framework import authentication, permissions

from ...models.workplace_models import WorkplaceModel
from ...serializers.workplace_serializers import WorkplaceSerializer


class WorkplacesListCreate(generics.ListCreateAPIView):
    queryset = WorkplaceModel.objects.all()
    serializer_class = WorkplaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


class WorkplaceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkplaceModel.objects.all()
    serializer_class = WorkplaceSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
