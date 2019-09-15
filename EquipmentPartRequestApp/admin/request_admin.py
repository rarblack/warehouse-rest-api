from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ..models.request_models import \
    RequestModel, \
    RequestUpdateModel


@admin.register(RequestModel)
class RequestAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'sap_number', 'manufacturer',
        'status', 'created_by', 'created_datetime'
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            request_update = RequestUpdateModel.objects.get(request=obj)
            request_update.created_by = request.user
            request_update.created_datetime = timezone.now()
            request_update.save()
        super().save_model(request, obj, form, change)

