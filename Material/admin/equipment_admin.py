from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ..models.equipment_models import EquipmentModel


@admin.register(EquipmentModel)
class EquipmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            device = FCMDevice.objects.all().first()
            device.send_message(title="TEST", body="THIS IS A TEST dsaf MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
        super().save_model(request, obj, form, change)

