from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from ...models.workplace.models import WorkplaceModel
from ...models.sap.models import SapModel


class EquipmentModel(models.Model):

    name = models.CharField(
        max_length=250
    )

    sap_number = models.IntegerField(
        null=True,
        blank=True,
        editable=False
    )

    sap = models.OneToOneField(
        SapModel,
        on_delete=models.CASCADE,
        related_name='equipment_part_request_app_equipment_model_sap_field'
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

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_equipment_model_updated_by_field',
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
        related_name='equipment_part_request_app_equipment_model_created_by_field',
        editable=False
    )

    created_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return 'Name: {0} SAP Number:{1}'.format(
            self.name, self.sap.sap_number
        )


@receiver(post_save, sender=EquipmentModel)
def update_sap_number(sender, instance, created, **kwargs):
    if created:
        instance.sap_number = instance.sap.sap_number
        instance.save()
    if not instance.sap_number == instance.sap.sap_number:
        instance.sap_number = instance.sap.sap_number
        instance.save()