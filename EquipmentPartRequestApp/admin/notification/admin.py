from django.contrib import admin
from django.utils import timezone

from ...models.notification import models


@admin.register(models.NotificationModel)
class NotificationAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'message', 'created_by', 'created_datetime')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            obj.updated_by = request.user
            obj.updated_datetime = timezone.now()
            obj.save()
        super().save_model(request, obj, form, change)

