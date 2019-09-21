from django.urls import path

from ....views.api.equipment_views import EquipmentRetrieveApiView


urlpatterns = [
    path(
        'retrieve/equipment/<int:sap_number>/',
        EquipmentRetrieveApiView.as_view()
    ),
]
