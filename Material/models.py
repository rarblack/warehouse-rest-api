from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from . import choices


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AbstractModel(models.Model):
    creation_datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Profile(AbstractModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='materials_profile_user')

    middle_name = models.CharField(max_length=30,
                                   blank=True)

    gender = models.IntegerField(choices=choices.GENDERS,
                                 null=True,
                                 default=0)

    employ_date = models.DateTimeField(null=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name="materials_profile_creator")

    def __str__(self):
        return self.user.username

    # def get_department_display_short(self):
    #     if self.department:
    #         return list(choices.DEPARTMENTS_SHORT)[self.department][1]

    def get_full_name(self):
        return '{0} {1}'.format(self.user.first_name,
                                self.user.last_name)

    def get_creator(self):
        return self.creator

    @receiver(post_save, sender=User)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, creator=instance)


STATUSES = (
    (0, 'Accepted'),
    (1, 'Pending'),
    (2, 'Closed'),
    (3, 'Cancelled')
)


def upload_to(instance, filename):
    return 'request_images/{0}'.format(filename)


class RequestModel(AbstractModel):

    image = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True
    )

    parts = models.ManyToManyField('PartModel')

    work_place = models.ForeignKey(
        'WorkPlaceModel',
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
        choices=STATUSES,
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

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'


class DeviceModel(AbstractModel):

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
        'WorkPlaceModel',
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

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'


class PartModel(AbstractModel):

    name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='material_part_creator'
    )

    def __str__(self):
        return '{0}: {1}'.format(self.id,
                                 self.name)

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'


class WorkPlaceModel(AbstractModel):
    name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='material_workplace_creator'
    )


class NotificationModel(AbstractModel):

    title = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    body = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    data = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='material_notification_creator'
    )

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
