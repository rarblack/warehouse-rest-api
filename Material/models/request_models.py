from django.db import models
from django.utils import timezone
from django.conf import settings

from .choices import request_choices as choices
from .workplace_models import WorkplaceModel
from .part_models import PartModel


def upload_image_to(instance, filename):
    return 'request_images/{0}'.format(filename)


class RequestModel(models.Model):

    image = models.ImageField(
        upload_to=upload_image_to,
        null=True,
        blank=True
    )

    parts = models.ManyToManyField(PartModel)

    work_place = models.ForeignKey(
        WorkplaceModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='material_request_workplace'
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

    processor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='material_request_processor',
    )

    procession_datetime = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='material_request_creator'
    )

    creation_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
