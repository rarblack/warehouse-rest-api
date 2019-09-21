from django.urls import path

from EquipmentPartRequestApp.views.api.request_views import \
    RequestTokenAuthenticatedDestroyApiView, \
    RequestTokenAuthenticatedUpdateApiView, \
    RequestsTokenAuthenticatedListApiView, \
    RequestTokenAuthenticatedCreateApiView, \
    RequestTokenAuthenticatedRetrieveApiView


urlpatterns = [
    path(
        'create/request/',
        RequestTokenAuthenticatedCreateApiView.as_view()
    ),

    path(
        'list/requests/',
        RequestsTokenAuthenticatedListApiView.as_view()
    ),

    path(
        'retrieve/request/<int:pk>/',
        RequestTokenAuthenticatedRetrieveApiView.as_view()
    ),

    path(
        'update/request/<int:pk>/',
        RequestTokenAuthenticatedUpdateApiView.as_view()
    ),

    path(
        'destroy/request/<int:pk>/',
        RequestTokenAuthenticatedDestroyApiView.as_view()
    ),

]
