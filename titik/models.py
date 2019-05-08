from django.contrib.gis.db import models
from django.utils import timezone

class koordinat(models.Model):
    nama = models.CharField(max_length=100)
    titik = models.PointField()
    keterangan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class polygon(models.Model):
    nama = models.CharField(max_length=100)
    ordinat = models.PolygonField()
    keterangan = models.CharField(max_length=200)