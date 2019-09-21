from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ...models.equipment import models
from ...models.part.models import PartModel


@admin.register(models.EquipmentModel)
class EquipmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_by', 'created_datetime')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "parts":
            kwargs["queryset"] = PartModel.objects.filter(created_by=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_datetime = timezone.now()
        elif change:
            device = FCMDevice.objects.all().first()
            device.send_message(
                title="TEST",
                body="THIS IS A TEST dsaf MESSAGE",
                data={"KEY": "THIS IS A TEST MESSAGE"}
            )
            obj.updated_by = request.user
            obj.updated_datetime = timezone.now()
            obj.save()
        super().save_model(request, obj, form, change)