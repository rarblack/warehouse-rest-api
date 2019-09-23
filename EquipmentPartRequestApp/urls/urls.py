from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('requests/', include('EquipmentPartRequestApp.urls.includes.request.urls')),
    path('dashboard/', include('EquipmentPartRequestApp.urls.includes.dashboard.url')),
]

urlpatterns += [
    path('api/equipments/', include('EquipmentPartRequestApp.urls.includes.api.equipment.urls')),
    path('api/firebase-cloud-messaging-devices/', include('EquipmentPartRequestApp.urls.includes.api.firebase_cloud_messaging_device.urls')),
    path('api/notifications/', include('EquipmentPartRequestApp.urls.includes.api.notification.urls')),
    path('api/parts/', include('EquipmentPartRequestApp.urls.includes.api.part.urls')),
    path('api/requests/', include('EquipmentPartRequestApp.urls.includes.api.request.urls')),
    path('api/requests/', include('EquipmentPartRequestApp.urls.includes.api.charts.pie.urls')),
    path('api/users/', include('EquipmentPartRequestApp.urls.includes.api.user.urls')),
    path('api/workplaces/', include('EquipmentPartRequestApp.urls.includes.api.workplace.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
