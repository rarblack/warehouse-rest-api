from EquipmentPartRequestApp.views.api.notification.views import NotificationsListAPIView
from django.urls import path

urlpatterns = [
    path(
        'list/notifications/',
        NotificationsListAPIView.as_view(),
        name='list_notifications'
    ),
]