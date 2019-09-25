from django.contrib import admin

from ...models.statistic import models


@admin.register(models.RequestCountPerPartStatisticalModel)
class RequestCountPerPartStatisticalAdmin(admin.ModelAdmin):

    list_display = (
        'part', 'count'
    )


@admin.register(models.RequestCountPerWorkplaceStatisticalModel)
class RequestCountPerWorkplaceStatisticalAdmin(admin.ModelAdmin):

    list_display = (
        'workplace', 'count'
    )


