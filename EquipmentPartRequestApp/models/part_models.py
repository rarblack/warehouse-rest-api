from django.db import models
from django.conf import settings
from django.utils import timezone


class PartModel(models.Model):

    name = models.CharField(
        max_length=250
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_part_creator'
    )

    created_datetime = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return '{0}: {1}'.format(self.id,
                                 self.name)

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        return self.name
