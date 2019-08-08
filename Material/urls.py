from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, re_path

urlpatterns = [
    # re_path(r'^api-token-auth/', obtain_auth_token),
    re_path(r'^api-token-auth/', views.CustomObtainAuthToken.as_view()),

    re_path('^create/request/', views.RequestCreateAPIView.as_view(), name='request_create'),
    re_path('^list/requests/', views.RequestsListAPIView.as_view(), name='request_list'),
    re_path('^retrieve/request/(?P<pk>\d+?)/', views.RequestRetrieveAPIView.as_view(), name='request_retrieve'),
    re_path('^update/request/(?P<pk>\d+?)/', views.RequestUpdateAPIView.as_view(), name='request_update'),
    re_path('^destroy/request/(?P<pk>\d+?)/', views.RequestDestroyAPIView.as_view(), name='request_destroy'),

    re_path('^create-list/parts/', views.CreateListParts.as_view(), name='parts_create_list'),
    re_path('^retrieve-update-destroy/part/(?P<pk>\d+?)/', views.PartRetrieveUpdateDestroy.as_view(), name='part_retrieve_update_destroy'),


    re_path('^create-list/work-places/', views.CreateListWorkPlaces.as_view(), name='work_places_create_list'),
    re_path('^retrieve-update-destroy/work-place/(?P<pk>\d+?)/', views.WorkPlaceRetrieveUpdateDestroy.as_view(), name='work_place_retrieve_update_destroy'),

    re_path('^retrieve/device/(?P<pk>\d+?)/', views.RetrieveDevice.as_view(), name='device_retrieve'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)