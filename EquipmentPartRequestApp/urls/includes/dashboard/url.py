from django.urls import path

from EquipmentPartRequestApp.views.dashboard.view import \
    DashboardTemplateView

urlpatterns = [
    path(
        '',
        DashboardTemplateView.as_view(),
        name='template_dashboard'
    ),
]
