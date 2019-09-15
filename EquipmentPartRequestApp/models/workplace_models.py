from django.db import models
from django.utils import timezone
from django.conf import settings


class WorkplaceModel(models.Model):

    name = models.CharField(
        max_length=250
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_workplace_creator'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = "Workplace"
        verbose_name_plural = "Workplaces"

    def __str__(self):
        return self.name
