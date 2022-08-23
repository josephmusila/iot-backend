from django.contrib import admin
from . import models

# Register your models here.
class SensorDataAdmin(admin.ModelAdmin):
    list_display=("id","date_created","time_added","temperature","photocell","waterlevel","soilmoisture",)


admin.site.register(models.Sensors,SensorDataAdmin)