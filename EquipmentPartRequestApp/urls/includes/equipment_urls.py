from ...views.api.equipment_views import DeviceRetrieveApiView
from django.urls import path

urlpatterns = [
    path(
        'retrieve/equipment/<int:pk>/',
        DeviceRetrieveApiView.as_view(),
        name='retrieve_device'
    ),
]
