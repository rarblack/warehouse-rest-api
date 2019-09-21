from django.urls import path

from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path(
        'create/firebase-cloud-messaging-device/',
        FCMDeviceAuthorizedViewSet.as_view(
            {'post': 'create'}),
        name='create_firebase_cloud_messaging_device'
    ),
]


