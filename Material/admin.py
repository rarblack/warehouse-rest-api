from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from django.contrib.auth.models import User

from fcm_django.models import FCMDevice

from .models import Profile, RequestModel, DeviceModel, PartModel, WorkPlaceModel


@admin.register(RequestModel)
class RequestAdmin(admin.ModelAdmin):

    list_display = ('id', 'sap_number', 'manufacturer', 'status', 'creator')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(DeviceModel)
class DeviceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        elif change:
            device = FCMDevice.objects.all().first()
            device.send_message(title="TEST", body="THIS IS A TEST MESSAGE", data={"KEY": "THIS IS A TEST MESSAGE"})
        super().save_model(request, obj, form, change)


@admin.register(PartModel)
class PartAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'creator')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(WorkPlaceModel)
class WorkPlaceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'creator')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
            obj.creation_datetime = timezone.now()
        super().save_model(request, obj, form, change)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
