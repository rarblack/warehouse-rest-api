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

    workplace = models.ForeignKey(
        WorkplaceModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_request_workplace'
    )

    sap_number = models.IntegerField()

    manufacturer = models.CharField(
        max_length=500
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

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_request_model_creator_field'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return ''


class RequestUpdateModel(models.Model):

    request = models.OneToOneField(
        RequestModel,
        on_delete=models.CASCADE,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_request_update_model_creator_field'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Request Update'
        verbose_name_plural = 'Request Updates'

    def __str__(self):
        return 'RequestId:{0} RequestUpdateId:{1}'.format(
            self.request.id,
            self.id
        )


