from django.urls import path

from EquipmentPartRequestApp.views.request_view import \
    RequestCreateView, \
    RequestUpdateView, \
    RequestDetailView

urlpatterns = [
    path(
        'create/request/',
        RequestCreateView.as_view(),
        name='create_request'
    ),

    path(
        'update/request/<int:pk>/',
        RequestUpdateView.as_view(),
        name='update_request'
    ),

    path(
        'detail/request/<int:pk>/',
        RequestDetailView.as_view(),
        name='detail_request'
    ),

    path(
        'accept/request/<int:pk>/',
        accept_request(),
        name='accept_request'
    ),

    path(
        'cancel/request/<int:pk>/',
        cancel_request(),
        name='cancel_request'
    ),

]