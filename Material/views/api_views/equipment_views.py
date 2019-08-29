from rest_framework import generics
from rest_framework import authentication, permissions

from ...serializers.equipment_serializers import EquipmentSerializer
from ...models.equipment_models import EquipmentModel


class DeviceRetrieveApiView(generics.RetrieveAPIView):
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)


