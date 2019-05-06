from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

class ruang(models.Model):
    nama = models.CharField(max_length=100)
    location = models.PolygonField()
    luas = models.CharField(max_length=100)
    distrik = models.CharField(max_length=50)
    kampung = models.CharField(max_length=50)