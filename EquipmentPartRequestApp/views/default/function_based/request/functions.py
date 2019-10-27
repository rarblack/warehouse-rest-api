from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .....models.response.models import ResponseModel
from .....models.request.models import RequestModel
from .....forms.model_forms.response.forms import ResponseModelForm
from .....shortcuts.views.functions import \
    send_notification, \
    record_notification


def accept_request(request, pk):

    request_object = get_object_or_404(RequestModel, pk=pk)
    if request_object:
        request_object.status = 1
        request_object.save()

        title = 'Request Status Changed'
        message = 'Your request {0} has been accepted'.format(
            request_object.id
        )

        device_id = request_object.device_id
        send_notification(device_id, title, message)

        record_notification(request_object, title, message, request.user)

        return HttpResponseRedirect(
            reverse('equipment_part_request_app:template_dashboard')
        )
    else:
        return HttpResponseRedirect(
            reverse('equipment_part_request_app:list_pending_requests'),

        )


def reject_request(request, pk):
    request_object = RequestModel.objects.get(
        pk=pk
    )
    response_object = ResponseModel.objects.create(
        request=request_object
    )

    device_id = request_object.device_id

    if request.method == 'POST':

        form = ResponseModelForm(request.POST)

        if form.is_valid():

            response_object.comment = form.cleaned_data['comment']
            response_object.created_by = request.user
            response_object.save()

            request_object.status = 2
            request_object.save()

            title = 'Request Status Changed'
            message = 'Your request {0} has been rejected'.format(
                request_object.id
            )
            send_notification(device_id, title, message)
            record_notification(title, message, request.user)

            return HttpResponseRedirect(
                reverse('equipment_part_request_app:template_dashboard')
            )
    else:

        form = ResponseModelForm()

    context = {
        'form': form
    }

    return render(
        request,
        'default/list/requests_list.html',
        context
    )



