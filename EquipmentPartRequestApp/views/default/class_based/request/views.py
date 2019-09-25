from django.views import generic
from django.contrib.auth import mixins

from EquipmentPartRequestApp.models.request.models import RequestModel


class RequestDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    model = RequestModel
    context_object_name = 'request'
    template_name = 'default/detail/request_detail.html'


class AllRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'default/list/requests_list.html'


class PendingRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=0)


class AcceptedRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=1)


class CancelledRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=2)


class ClosedRequestsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = RequestModel
    context_object_name = 'requests'
    template_name = 'default/list/requests_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status__exact=3)
