from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.gis.db import models

# Create your models here.
class Station(models.Model):
    station_name = models.CharField(max_length=300)
    station_region = models.CharField(max_length=30)
    station_node = models.CharField(max_length=30)
    station_fuel = models.CharField(max_length=30)
    station_type = models.CharField(max_length=30)
    station_year = models.CharField(max_length=30)
    station_capacity = models.CharField(max_length=30)
    station_efficiency = models.CharField(max_length=30)
    station_mc = models.CharField(max_length=30)
    station_min_load = models.CharField(max_length=30)
    station_min_winter = models.CharField(max_length=30)
    station_min_summer = models.CharField(max_length=30)
    station_availability_winter = models.CharField(max_length=30)
    station_availability_summer = models.CharField(max_length=30)
    station_emission = models.CharField(max_length=30)
    station_location_long = models.FloatField() # longitude
    station_location_lat = models.FloatField() # latitude
    
    def __str__(self) -> str:
        return self.station_name

class CustomUser(AbstractUser):

    # field to store user picture
    user_avatar = models.ImageField(upload_to="user_avatars/", default='NULL')

    # returning username when called
    def __str__(self) -> str:
        return self.username