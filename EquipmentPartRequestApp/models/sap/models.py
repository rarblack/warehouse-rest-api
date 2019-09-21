from django.db import models
from django.conf import settings
from django.utils import timezone


class SapModel(models.Model):

    sap_number = models.IntegerField(
        unique=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_sap_model_created_by_field'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'SAP'
        verbose_name_plural = 'SAP'

    def __str__(self):
        return '{0}'.format(
            self.sap_number
        )
