from django.contrib import admin
from main.models import Manufacturer, Cereal


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CerealAdmin(admin.ModelAdmin):
    list_display = ('name', 'manuf', 'cer_type',
                    'calories', 'protein', 'fat', 'sodium',
                    'fiber', 'carbs', 'sugars', 'potassium',
                    'vits_mins', 'ss_weight', 'cups_per_s')


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Cereal, CerealAdmin)
