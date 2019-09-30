from rest_framework import generics
from rest_framework import authentication, permissions

from ....serializers.equipment import serializers
from ....models.equipment.models import EquipmentModel


class EquipmentRetrieveApiView(generics.RetrieveAPIView):
    lookup_field = 'sap_number'
    queryset = EquipmentModel.objects.all()
    serializer_class = serializers.EquipmentSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)