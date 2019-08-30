from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .choices import user_choices as choices


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='equipment_part_request_apps_profile_user'
    )

    middle_name = models.CharField(
        max_length=30,
        blank=True
    )

    gender = models.IntegerField(
        choices=choices.GENDERS,
        null=True,
        default=0
    )

    employ_date = models.DateTimeField(
        null=True
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="equipment_part_request_apps_profile_creator"
    )

    creation_datetime = models.DateTimeField(
        default=timezone.now
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
        return self.creator

    @receiver(post_save, sender=User)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, creator=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)