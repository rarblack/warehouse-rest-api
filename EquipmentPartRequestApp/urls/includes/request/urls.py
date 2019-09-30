from django.urls import path

from EquipmentPartRequestApp.views.default.class_based.request.views import \
    RequestDetailView, \
    AllRequestsListView, \
    PendingRequestsListView, \
    AcceptedRequestsListView, \
    CancelledRequestsListView, \
    ClosedRequestsListView

from ....views.default.method_based.request.methods import \
    accept_request, \
    reject_request


urlpatterns = [

    path(
        'detail/request/<int:pk>/',
        RequestDetailView.as_view(),
        name='detail_request'
    ),

    path(
        'list/all/requests/',
        AllRequestsListView.as_view(),
        name='list_all_requests'
    ),

    path(
        'list/pending/requests/',
        PendingRequestsListView.as_view(),
        name='list_pending_requests'
    ),

    path(
        'list/accepted/requests/',
        AcceptedRequestsListView.as_view(),
        name='list_accepted_requests'
    ),

    path(
        'list/rejected/requests/',
        CancelledRequestsListView.as_view(),
        name='list_rejected_requests'
    ),
    path(
        'list/closed/requests/',
        ClosedRequestsListView.as_view(),
        name='list_closed_requests'
    ),

    path(
        'accept/request/<int:pk>/',
        accept_request,
        name='accept_request'
    ),

    path(
        'reject/request/<int:pk>/',
        reject_request,
        name='reject_request'
    ),
]
