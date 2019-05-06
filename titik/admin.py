from django.contrib.gis import admin

from .models import koordinat, polygon

admin.site.register(koordinat, admin.GeoModelAdmin)
admin.site.register(polygon, admin.GeoModelAdmin)