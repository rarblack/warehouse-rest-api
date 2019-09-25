from django.db import models
from django.utils import timezone
from django.conf import settings


from ...models.response.choices import CAUSES
from ...models.request.models import RequestModel


class ResponseModel(models.Model):

    request = models.ForeignKey(
        RequestModel,
        on_delete=models.CASCADE,
        related_name='equipment_part_request_app_respond_model_request_field'
    )

    comment = models.TextField(
        max_length=700,
        blank=True,
        null=True
    )

    # cause = models.IntegerField(
    #     choices=CAUSES,
    #     default=0
    # )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_response_model_updated_by_field',
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
        related_name='equipment_part_request_app_response_model_created_by_field',
        editable=False
    )

    created_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'

    def __str__(self):
        return 'Response to request id {0}'.format(
            self.request.id
        )
