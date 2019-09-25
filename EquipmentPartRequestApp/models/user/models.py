from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from ...models.user import choices


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='equipment_part_request_app_profile_model_user_field'
    )

    middle_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    gender = models.IntegerField(
        choices=choices.GENDERS,
        null=True,
        default=0
    )

    employed_datetime = models.DateTimeField(
        null=True,
        blank=True
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='equipment_part_request_app_profile_model_updated_by_field',
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
        related_name="equipment_part_request_app_profile_model_created_by_field",
        editable=False
    )

    created_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    def __str__(self):
        return self.user.username

    # def get_department_display_short(self):
    #     if self.department:
    #         return list(choices.DEPARTMENTS_SHORT)[self.department][1]

    def get_full_name(self):
        return '{0} {1}'.format(self.user.first_name,
                                self.user.last_name)

    def get_creator(self):
        return self.created_by

    @receiver(post_save, sender=User)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, created_by=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)