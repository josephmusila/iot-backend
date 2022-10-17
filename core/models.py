from django.db import models

# Create your models here.

class Sensors(models.Model):
    photocell=models.CharField(null=True,blank=True,max_length=5)
    waterlevel=models.CharField(null=True,blank=True,max_length=5)
    soilmoisture=models.CharField(null=True,blank=True,max_length=5)
    temperature=models.CharField(null=True,blank=True,max_length=5)
    time_added=models.TimeField(auto_now_add=True,blank=True)
    date_created=models.DateField(auto_now_add=True,null=True,blank=True)

 