from django.db import models
from django.conf import settings
from django.utils import timezone

from .workplace_models import WorkplaceModel
from .sap.models import SapModel


class EquipmentModel(models.Model):

    name = models.CharField(
        max_length=250
    )

    sap = models.OneToOneField(
        SapModel,
        on_delete=models.CASCADE
    )

    manufacturer = models.CharField(
        max_length=500
    )

    parts = models.ManyToManyField('PartModel')

    workplace = models.ForeignKey(
        WorkplaceModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_equipment_model_workplace_field'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_equipment_model_created_by_field'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return 'Name: {0} SAP Number:{1}'.format(
            self.name, self.sap.sap_number
        )
