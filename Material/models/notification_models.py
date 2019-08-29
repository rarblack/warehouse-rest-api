from django.db import models
from django.utils import timezone
from django.conf import settings


class NotificationModel(models.Model):

    title = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    body = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    data = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='material_notification_creator'
    )

    creation_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
