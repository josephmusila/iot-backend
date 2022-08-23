from django.db import models

# Create your models here.


class Sensors(models.Model):
    photocell=models.IntegerField(null=True,blank=True)
    waterlevel=models.IntegerField(null=True,blank=True)
    soilmoisture=models.IntegerField(null=True,blank=True)

    temperature=models.DecimalField(decimal_places=2,max_digits=5,null=True,blank=True)
    time_added=models.TimeField(auto_now_add=True,blank=True)
    date_created=models.DateField(auto_now_add=True,null=True,blank=True)

