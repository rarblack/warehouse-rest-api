from django.urls import path

from EquipmentPartRequestApp.views.request.view import \
    RequestDetailView, \
    AllRequestsListView, \
    PendingRequestsListView, \
    AcceptedRequestsListView, \
    CancelledRequestsListView, \
    ClosedRequestsListView, \
    accept_request, \
    cancel_request

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
        'list/cancelled/requests/',
        CancelledRequestsListView.as_view(),
        name='list_cancelled_requests'
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
        'cancel/request/<int:pk>/',
        cancel_request,
        name='cancel_request'
    ),
]
