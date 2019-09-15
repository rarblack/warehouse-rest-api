from django.urls import path

from EquipmentPartRequestApp.views.api_views.request_views import \
    RequestDestroyApiView,\
    RequestUpdateApiView,\
    RequestsListApiView,\
    RequestCreateApiView,\
    RequestRetrieveApiView


urlpatterns = [
    path(
        'create/request/',
        RequestCreateApiView.as_view()
    ),

    path(
        'list/requests/',
        RequestsListApiView.as_view()
    ),

    path(
        'retrieve/request/<int:pk>/',
        RequestRetrieveApiView.as_view()
    ),

    path(
        'update/request/<int:pk>/',
        RequestUpdateApiView.as_view()
    ),

    path(
        'destroy/request/<int:pk>/',
        RequestDestroyApiView.as_view()
    ),

]