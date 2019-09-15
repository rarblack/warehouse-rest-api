from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ..models.equipment_models import EquipmentModel
from ..models.part_models import PartModel


@admin.register(EquipmentModel)
class EquipmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_by', 'created_datetime')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "parts":
            kwargs["queryset"] = PartModel.objects.filter(creator=2)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            device = FCMDevice.objects.all().first()
            device.send_message(title="TEST", body="THIS IS A TEST dsaf MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
        super().save_model(request, obj, form, change)
