from django.views import generic

from ..models.request_models import \
    RequestModel


class DashboardTemplateView(generic.TemplateView):
    template_name = 'equipment_part_request_app/default/list/requests_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_requests = get_all_requests()
        context["requests"] = all_requests
        context["count_all_requests"] = len(all_requests)
        return context


def get_all_requests():
    return RequestModel.objects.all()


def get_filtered_requests(status):
    return RequestModel.objects.filter(status__exact=status)


def get_most_requested_equipment():
    return None


def get_most_requested_part():
    return None


def get_most_request_came_workplace():
    return None
