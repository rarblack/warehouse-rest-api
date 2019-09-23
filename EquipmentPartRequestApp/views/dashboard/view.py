from django.views import generic
from django.contrib.auth import mixins

from ...models.request.models import RequestModel


class DashboardTemplateView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'equipment_part_request_app/../../templates/default/template/dashboard_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_requests_length = get_all_requests_length()
        pending_requests_length = get_pending_requests_length()
        accepted_requests_length = get_accepted_requests_length()
        cancelled_requests_length = get_cancelled_requests_length()
        closed_requests_length = get_closed_requests_length()

        pending_requests_percent = round((pending_requests_length/all_requests_length)*100, 2) if all_requests_length < 0 else 0
        accepted_requests_percent = round((accepted_requests_length/all_requests_length)*100, 2) if all_requests_length < 0 else 0
        cancelled_requests_percent = round((cancelled_requests_length/all_requests_length)*100, 2) if all_requests_length < 0 else 0
        closed_requests_percent = round((closed_requests_length/all_requests_length)*100, 2) if all_requests_length < 0 else 0

        context["all_requests_length"] = all_requests_length
        context['pending_requests_length'] = pending_requests_length
        context['accepted_requests_length'] = accepted_requests_length
        context['cancelled_requests_length'] = cancelled_requests_length
        context['closed_requests_length'] = closed_requests_length

        context['pending_requests_percent'] = pending_requests_percent
        context['accepted_requests_percent'] = accepted_requests_percent
        context['cancelled_requests_percent'] = cancelled_requests_percent
        context['closed_requests_percent'] = closed_requests_percent
        return context


def get_all_requests_length():
    return len(RequestModel.objects.all())


def get_pending_requests_length():
    return len(RequestModel.objects.filter(status__exact=0))


def get_accepted_requests_length():
    return len(RequestModel.objects.filter(status__exact=1))


def get_cancelled_requests_length():
    return len(RequestModel.objects.filter(status__exact=2))


def get_closed_requests_length():
    return len(RequestModel.objects.filter(status__exact=3))


def get_most_requested_equipment():
    return None


def get_most_requested_part():
    return None


def get_most_request_came_workplace():
    return None
