from django.db import models
from django.utils import timezone
from django.conf import settings

from ...models.equipment.models import EquipmentModel
from ...models.part.models import PartModel
from ...models.request import choices


def upload_image_to(instance, filename):
    return 'request_images/{0}'.format(filename)


class RequestModel(models.Model):

    image = models.ImageField(
        upload_to=upload_image_to,
        null=True,
        blank=True
    )

    equipment = models.ForeignKey(
        EquipmentModel,
        on_delete=models.CASCADE
    )
    parts = models.ManyToManyField(PartModel)

    quantity = models.IntegerField(default=0)

    size = models.IntegerField(default=0)

    weight = models.IntegerField(default=0)

    comment = models.TextField(
        max_length=700,
        blank=True,
        null=True
    )

    status = models.IntegerField(
        choices=choices.STATUSES,
        default=0
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_request_model_updated_by_field'
    )

    updated_datetime = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_request_model_created_by_field'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return '{0} part request'.format(
            self.equipment.name
        )
