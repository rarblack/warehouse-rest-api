from rest_framework import generics

from EquipmentPartRequestApp.serializers.request.serializers import RequestSerializer
from EquipmentPartRequestApp.models.request.models import RequestModel


class RequestsListApiView(generics.ListAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
