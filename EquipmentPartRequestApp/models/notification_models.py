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

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_notification_creator'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return self.title
