from rest_framework import generics
from rest_framework import authentication, permissions

from ...serializers.equipment_serializers import EquipmentSerializer
from ...models.equipment_models import EquipmentModel


class EquipmentRetrieveApiView(generics.RetrieveAPIView):
    lookup_field = 'sap_number'
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentSerializer
    # authentication_classes = (authentication.TokenAuthentication, )
    # permission_classes = (permissions.IsAuthenticated,)


