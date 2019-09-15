from django.contrib import admin
from django.utils import timezone

from fcm_django.models import FCMDevice

from ..models.notification_models import NotificationModel


@admin.register(NotificationModel)
class NotificationAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'body', 'data', 'created_by')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        super().save_model(request, obj, form, change)

