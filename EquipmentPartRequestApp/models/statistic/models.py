from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from ...models.request.models import RequestModel
from ...models.part.models import PartModel
from ...models.workplace.models import WorkplaceModel


class RequestCountPerPartStatisticalModel(models.Model):

    part = models.OneToOneField(
        PartModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_request_count_per_part_statistical_model_part_field'
    )

    count = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Count of the requests per part'
        verbose_name_plural = 'Count of the requests per parts'


@receiver(m2m_changed, sender=RequestModel.parts.through)
def request_parts_changed(sender, action, instance, **kwargs):

    pk_set = kwargs['pk_set']
    model = RequestCountPerPartStatisticalModel

    if action == 'post_remove':
        for pk in pk_set:
            obj = model.objects.get(part_id=pk)
            if not obj.count == 0:
                obj.count -= 1
                obj.save()
            obj.delete()

    if action == 'post_add':
        for pk in pk_set:
            obj, created = model.objects.get_or_create(part_id=pk)
            if not created:
                obj.count += 1
                obj.save()


class RequestCountPerWorkplaceStatisticalModel(models.Model):

    workplace = models.OneToOneField(
        WorkplaceModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='equipment_part_request_app_request_count_per_workplace_statistical_model_workplace_field'
    )

    count = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Count of the requests per workplace'
        verbose_name_plural = 'Count of the requests per workplaces'

    @receiver(post_save, sender=RequestModel)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        print(kwargs['update_fields'])
        if created:
            obj, new = RequestCountPerWorkplaceStatisticalModel.objects.get_or_create(
                workplace=instance.equipment.workplace
            )
            if not new:
                obj.count += 1
                obj.save()
