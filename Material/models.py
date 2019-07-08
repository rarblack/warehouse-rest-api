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

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='materials_profile_user')

    middle_name = models.CharField(max_length=30,
                                   blank=True)

    gender = models.IntegerField(choices=choices.GENDERS,
                                 null=True,
                                 default=0)

    employ_date = models.DateTimeField(null=True)

    creator = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name="materials_profile_creator")

    def __str__(self):
        return self.user.username

    # def get_department_display_short(self):
    #     if self.department:
    #         return list(choices.DEPARTMENTS_SHORT)[self.department][1]

    def get_full_name(self):
        return '{} {}'.format(self.user.first_name,
                              self.user.last_name)

    def get_creator(self):
        return self.creator

    @receiver(post_save, sender=User)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, creator=instance)


def upload_file_to(instance, filename):
    return f'materials/filename'


class MaterialsModel(AbstractModel):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='materials_materialsModel_user')
    file = models.FileField(upload_to=upload_file_to,
                            null=True)

    order = models.IntegerField(null=True,
                                default=0,
                                blank=0)

    parts = models.IntegerField(null=True,
                                default=0,
                                blank=0)

    quantity = models.IntegerField(null=True,
                                   default=0,
                                   blank=0)

    comment = models.TextField(max_length=700,
                               blank=True,
                               null=True)