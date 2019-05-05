from django.contrib.gis import admin
from .models import Shop

admin.site.register(Shop, admin.GeoModelAdmin)