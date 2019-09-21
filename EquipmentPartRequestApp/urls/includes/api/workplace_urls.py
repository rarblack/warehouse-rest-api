from django.urls import path
from EquipmentPartRequestApp.views.api.workplace_views import \
    WorkplacesListCreate,\
    WorkplaceRetrieveUpdateDestroy

urlpatterns = [
    path(
        'create/workplace/',
        WorkplacesListCreate.as_view(),
        name='create_workplace'
    ),

    path(
        'list/workplaces/',
        WorkplacesListCreate.as_view(),
        name='list_workplaces'
    ),

    path(
        'retrieve/workplace/<int:pk>/',
        WorkplaceRetrieveUpdateDestroy.as_view(),
        name='retrieve_workplace'
    ),

    path(
        'update/workplace/<int:pk>/',
        WorkplaceRetrieveUpdateDestroy.as_view(),
        name='update_workplace'
    ),

    path(
        'destroy/workplace/<int:pk>/',
        WorkplaceRetrieveUpdateDestroy.as_view(),
        name='destroy_workplace'
    ),
]