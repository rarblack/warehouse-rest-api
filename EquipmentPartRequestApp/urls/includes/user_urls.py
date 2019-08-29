from django.urls import path

from ...views.api_views.user_views import CustomObtainAuthToken

urlpatterns = [
    path(
        'api-token-auth/',
        CustomObtainAuthToken.as_view()
    ),
]
