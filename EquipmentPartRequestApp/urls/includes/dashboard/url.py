from django.urls import path

from EquipmentPartRequestApp.views.default.class_based.dashboard.views import \
    DashboardTemplateView

urlpatterns = [
    path(
        '',
        DashboardTemplateView.as_view(),
        name='template_dashboard'
    ),
]
