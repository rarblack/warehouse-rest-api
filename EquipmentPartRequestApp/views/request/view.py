from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from ...models.request.models import RequestModel


class RequestDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    model = RequestModel
    context_object_name = 'request'
    template_name = 'equipment_part_request_app/default/detail/request_detail.html'


class AllRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'equipment_part_request_app/default/list/requests_list.html'


class PendingRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'equipment_part_request_app/default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=0)


class AcceptedRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'equipment_part_request_app/default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=1)


class CancelledRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'equipment_part_request_app/default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=2)


class ClosedRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'equipment_part_request_app/default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=3)


def accept_request(request, pk):
    selected_request = get_object_or_404(RequestModel, pk=pk)
    selected_request.status = 1
    selected_request.save()

    return HttpResponseRedirect(
        reverse('equipment_part_request_app:template_dashboard')
    )


def cancel_request(request, pk):
    selected_request = get_object_or_404(RequestModel, pk=pk)
    selected_request.status = 2
    selected_request.save()

    return HttpResponseRedirect(
        reverse('equipment_part_request_app:template_dashboard')
    )
