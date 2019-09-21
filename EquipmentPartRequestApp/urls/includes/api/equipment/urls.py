from django.urls import path

from EquipmentPartRequestApp.views.api.equipment.views import EquipmentRetrieveApiView


urlpatterns = [
    path(
        'retrieve/equipment/<int:sap_number>/',
        EquipmentRetrieveApiView.as_view()
    ),
]
