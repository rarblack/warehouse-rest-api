from django.urls import path

from ...views.api_views.part_views import \
    PartRetrieveUpdateDestroyApiView, \
    PartsListCreateApiView

urlpatterns = [
    path(
        'create/part/',
        PartsListCreateApiView.as_view(),
        name='create_part'
    ),

    path(
        'list/parts/',
        PartsListCreateApiView.as_view(),
        name='list_parts'
    ),

    path(
        'retrieve/part/<int:pk>/',
        PartRetrieveUpdateDestroyApiView.as_view(),
        name='retrieve_part'
    ),

    path(
        'update/part/<int:pk>/',
        PartRetrieveUpdateDestroyApiView.as_view(),
        name='update_part'
    ),

    path(
        'destroy/part/<int:pk>/',
        PartRetrieveUpdateDestroyApiView.as_view(),
        name='destroy_part'
    ),
]