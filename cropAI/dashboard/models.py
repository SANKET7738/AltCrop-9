from django.db import models

# Create your models here.

class CropDetails(models.Model):
    State_Name_Label = models.PositiveSmallIntegerField(blank=False)
    State_Name = models.CharField(max_length=100,blank=False)
    District_Name_Label = models.PositiveSmallIntegerField(blank=False)
    District_Name = models.CharField(max_length=100,blank=False)
    Season_Label = models.PositiveSmallIntegerField(default=4)
    Season = models.CharField(max_length=50)
    Crop_Label = models.PositiveSmallIntegerField(blank=False)
    Crop = models.CharField(max_length=50)
    Area = models.FloatField()
    Production = models.FloatField()
    ANNUAL_RAIN = models.FloatField()
    KHARIF_RAIN = models.FloatField()
    RABI_RAIN = models.FloatField()
    SUMMER_RAIN = models.FloatField()
    ANNUAL_GROUND_WATER = models.FloatField()
    ANNUAL_GROUND_WATER_FOR_IRRIGATION = models.FloatField()

class ExtraInfo(models.Model):
    Crop = models.CharField(max_length=200)
    fertilizer_url = models.CharField(max_length=200)
    pesticide_url = models.CharField(max_length=200)
    seeds_url = models.CharField(max_length=200)
    method_url = models.CharField(max_length=200)
