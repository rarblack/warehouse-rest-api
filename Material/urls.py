from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^api-token-auth/', obtain_auth_token),
    re_path('^create-list/requests/', views.CreateListRequests.as_view(), name='requests_create_list'),
    re_path('^create-list/parts/', views.CreateListParts.as_view(), name='parts_create_list'),
    re_path('^create-list/work-places/', views.CreateListWorkPlaces.as_view(), name='work_places_create_list'),

    re_path('^retrieve/device/(?P<pk>\d+?)/', views.RetrieveDevice.as_view(), name='device_retrieve'),

    re_path('^retrieve-update-destroy/request/(?P<pk>\d+?)/', views.RequestRetrieveUpdateDestroy.as_view(), name='request_retrieve_update_destroy'),
    re_path('^retrieve-update-destroy/part/(?P<pk>\d+?)/', views.PartRetrieveUpdateDestroy.as_view(), name='request_retrieve_update_destroy'),
    re_path('^retrieve-update-destroy/work-place/(?P<pk>\d+?)/', views.WorkPlaceRetrieveUpdateDestroy.as_view(), name='request_retrieve_update_destroy'),
]