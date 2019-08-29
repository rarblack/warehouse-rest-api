from django.urls import path

from ...views.api_views.request_views import \
    RequestDestroyApiView,\
    RequestUpdateApiView,\
    RequestsListApiView,\
    RequestCreateApiView,\
    RequestRetrieveApiView

urlpatterns = [
    path(
        'create/request/',
        RequestCreateApiView.as_view(),
        name='create_request'
    ),

    path(
        'list/requests/',
        RequestsListApiView.as_view(),
        name='list_requests'
    ),

    path(
        'retrieve/request/<int:pk>/',
        RequestRetrieveApiView.as_view(),
        name='retrieve_request'
    ),

    path(
        'update/request/<int:pk>/',
        RequestUpdateApiView.as_view(),
        name='update_request'
    ),

    path(
        'destroy/request/<int:pk>/',
        RequestDestroyApiView.as_view(),
        name='destroy_request'
    ),

]