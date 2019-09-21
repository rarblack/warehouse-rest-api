from django.contrib import admin

from ...models.sap.models import SapModel


@admin.register(SapModel)
class SapAdmin(admin.ModelAdmin):

    list_display = (
        'sap_number', 'created_by', 'created_datetime'
    )

