from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

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

    # MATERIALS
    re_path(
        '',
        include(
            ('EquipmentPartRequestApp.urls.urls', 'Material'),
            namespace='equipment_part_request_app'
        )
    ),
]


