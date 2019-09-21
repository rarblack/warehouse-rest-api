from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_url = ''
admin.site.site_header = 'WarehouseAPI ADMIN'
admin.site.site_title = 'WarehouseAPI'
admin.site.index_title = 'Admin'
admin.empty_value_display = '**Empty**'

urlpatterns = [

    # DJANGO JET2
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    # ADMIN
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # EQUIPMENT_PART_REQUEST_APP
    path(
        '',
        include(
            ('EquipmentPartRequestApp.urls.urls', 'EquipmentPartRequestApp'),
            namespace='equipment_part_request_app'
        )
    ),

]
if settings.DEBUG:

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



