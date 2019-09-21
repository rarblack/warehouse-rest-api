from django.contrib import admin

from EquipmentPartRequestApp.models.statistic_model import \
    MostRequestedPartModel


@admin.register(MostRequestedPartModel)
class MostRequestedPartAdmin(admin.ModelAdmin):

    list_display = (
        'part', 'count'
    )

