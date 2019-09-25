from django.db import models
from django.utils import timezone
from django.conf import settings


class NotificationModel(models.Model):

    title = models.CharField(
        max_length=250
    )

    body = models.CharField(
        max_length=250
    )

    data = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_notification_model_updated_by_field',
        editable=False
    )

    updated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_notification_model_created_by_field',
        editable=False
    )

    created_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return self.title
