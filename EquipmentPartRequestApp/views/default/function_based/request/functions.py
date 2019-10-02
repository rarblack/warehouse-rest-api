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
    request_instance = get_object_or_404(RequestModel, pk=pk)
    request_instance.status = 1
    request_instance.save()

    title = 'Request Status Changed'
    message = 'Your request #{0} has been accepted'.format(
        request_instance.id
    )
    send_notification(title, message)
    record_notification(title, message, request.user)

    return HttpResponseRedirect(
        reverse('equipment_part_request_app:template_dashboard')
    )


def reject_request(request, pk):
    request_instance = RequestModel.objects.get(
        pk=pk
    )
    response_instance = ResponseModel.objects.create(
        request=request_instance
    )

    device_id = request_instance.device_id

    if request.method == 'POST':

        form = ResponseModelForm(request.POST)

        if form.is_valid():

            response_instance.comment = form.cleaned_data['comment']
            response_instance.created_by = request.user
            response_instance.save()

            request_instance.status = 2
            request_instance.save()

            title = 'Request Status Changed'
            message = 'Your request #{0} has been rejected'.format(
                request_instance.id
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



