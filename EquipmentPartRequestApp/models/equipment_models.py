from django.db import models
from django.conf import settings
from django.utils import timezone

from .workplace_models import WorkplaceModel


class EquipmentModel(models.Model):

    name = models.CharField(
        max_length=250
    )

    sap_number = models.IntegerField()

    manufacturer = models.CharField(
        max_length=500
    )

    parts = models.ManyToManyField('PartModel')

    workplace = models.ForeignKey(
        WorkplaceModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_device_workplace'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_device_creator'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return 'Name: {0} SAP:{1}'.format(
            self.name, self.sap_number
        )
