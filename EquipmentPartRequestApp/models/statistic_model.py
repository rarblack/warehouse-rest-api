from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.request_models import \
    RequestModel


class MostRequestedPartModel(models.Model):

    part = models.OneToOneField(
        RequestModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_statistic_model_part_field'
    )

    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Most Requested Part'
        verbose_name_plural = 'Most Requested Parts'


@receiver(post_save, sender=RequestModel)
def create_or_update_user_account(sender, instance, created, **kwargs):
    if created:
        print(instance.parts.all())
        print(instance.sap_number)
        print(instance.parts)
        for part in instance.parts.all():
            obj = MostRequestedPartModel.objects.get(part=part)
            if obj:
                obj.count += 1
                obj.save()
            MostRequestedPartModel.objects.create(
                part=part,
                count=1
            )
