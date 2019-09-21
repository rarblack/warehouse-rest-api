from django.urls import path

from EquipmentPartRequestApp.views.api.user_views import CustomObtainAuthToken

urlpatterns = [
    path(
        'api-token-auth/',
        CustomObtainAuthToken.as_view()
    ),
]
