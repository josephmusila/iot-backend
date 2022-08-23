from rest_framework import serializers
from .models import Sensors
class GetSensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model=Sensors
        fields=("photocell","waterlevel","soilmoisture","temperature","time_added","date_created")

