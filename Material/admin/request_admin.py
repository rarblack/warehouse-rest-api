from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ..models import request_models as models


@admin.register(models.RequestModel)
class RequestAdmin(admin.ModelAdmin):

    list_display = ('id', 'sap_number', 'manufacturer', 'status', 'creator')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            obj.processor = request.user
            obj.procession_datetime = timezone.now()
        super().save_model(request, obj, form, change)

