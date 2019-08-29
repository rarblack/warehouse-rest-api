from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('equipments/', include('Material.urls.includes.equipment_urls')),
    path('firebase-cloud-messaging-devices/', include('Material.urls.includes.firebase_cloud_messaging_device_urls')),
    path('notifications/', include('Material.urls.includes.notification_urls')),
    path('parts/', include('Material.urls.includes.part_urls')),
    path('requests/', include('Material.urls.includes.request_urls')),
    path('users/', include('Material.urls.includes.user_urls')),
    path('workplace/', include('Material.urls.includes.workplace_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
