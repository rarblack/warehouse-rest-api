from django.contrib import admin
from django.utils import timezone

from ...models.workplace import models


@admin.register(models.WorkplaceModel)
class WorkPlaceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            obj.updated_by = request.user
            obj.updated_datetime = timezone.now()
            obj.save()
        super().save_model(request, obj, form, change)

