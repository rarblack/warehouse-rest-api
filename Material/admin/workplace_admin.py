from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ..models import workplace_models as models


@admin.register(models.WorkplaceModel)
class WorkPlaceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'creator')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        super().save_model(request, obj, form, change)
