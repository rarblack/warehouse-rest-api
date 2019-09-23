from django.urls import path

from EquipmentPartRequestApp.views.api.user.views import CustomObtainAuthToken

urlpatterns = [
    path(
        'token-auth/',
        CustomObtainAuthToken.as_view()
    ),
]
