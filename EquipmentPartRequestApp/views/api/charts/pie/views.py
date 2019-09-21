from rest_framework import generics

from .....serializers.request_serializers import RequestSerializer
from .....models.request_models import RequestModel


class RequestsListApiView(generics.ListAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
