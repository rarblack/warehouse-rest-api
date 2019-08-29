from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('equipments/', include('EquipmentPartRequestApp.urls.includes.equipment_urls')),
    path('firebase-cloud-messaging-devices/', include('EquipmentPartRequestApp.urls.includes.firebase_cloud_messaging_device_urls')),
    path('notifications/', include('EquipmentPartRequestApp.urls.includes.notification_urls')),
    path('parts/', include('EquipmentPartRequestApp.urls.includes.part_urls')),
    path('requests/', include('EquipmentPartRequestApp.urls.includes.request_urls')),
    path('users/', include('EquipmentPartRequestApp.urls.includes.user_urls')),
    path('workplace/', include('EquipmentPartRequestApp.urls.includes.workplace_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
