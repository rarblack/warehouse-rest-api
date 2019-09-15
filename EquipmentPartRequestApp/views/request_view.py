from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from ..models.request_models import RequestModel


class RequestCreateView(generic.CreateView):
    model = RequestModel
    template_name = 'equipment_part_request_app/default/create/request_create.html'
    success_url = reverse('equipment_part_request_app:detail_request')


class RequestUpdateView(generic.UpdateView):
    model = RequestModel
    fields = [
        'parts', 'sap_number', 'workplace',
        'manufacturer', 'quantity', 'size',
        'weight', 'comment', 'status',
    ]


class RequestDetailView(generic.DetailView):
    model = RequestModel


def accept_request(request, pk):
    selected_request = get_object_or_404(RequestModel, pk=pk)
    selected_request.status = 1
    selected_request.save()

    return HttpResponseRedirect(reverse('equipment_parts_request_app:template_dashboard'))


def cancel_request(request, pk):
    selected_request = get_object_or_404(RequestModel, pk=pk)
    selected_request.status = 1
    selected_request.save()

    return HttpResponseRedirect(reverse('equipment_parts_request_app:template_dashboard'))