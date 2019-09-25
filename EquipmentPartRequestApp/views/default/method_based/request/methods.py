from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .....models.response.models import ResponseModel
from .....models.request.models import RequestModel
from .....forms.model_forms.response.forms import ResponseModelForm


def accept_request(request, pk):
    selected_request = get_object_or_404(RequestModel, pk=pk)
    selected_request.status = 1
    selected_request.save()

    return HttpResponseRedirect(
        reverse('equipment_part_request_app:template_dashboard')
    )


def cancel_request(request, request_id):
    request_instance = RequestModel.objects.get(
        pk=request_id
    )
    response_instance = ResponseModel.objects.create(
        request=request_instance
    )

    if request.method == 'POST':

        form = ResponseModelForm(request.POST)

        if form.is_valid():

            response_instance.comment = form.cleaned_data['comment']
            response_instance.created_by = request.user
            response_instance.save()

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
        'default/detail/request_detail.html',
        context
    )

