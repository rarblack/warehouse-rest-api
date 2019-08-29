from django.db import models
from django.conf import settings
from django.utils import timezone

from .workplace_models import WorkplaceModel


class EquipmentModel(models.Model):

    name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    sap_number = models.IntegerField(
        null=True,
        default=0,
        blank=True
    )

    manufacturer = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    parts = models.ManyToManyField('PartModel')

    work_place = models.ForeignKey(
        WorkplaceModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='material_device_workplace'
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='material_device_creator'
    )

    creation_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
