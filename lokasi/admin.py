from django.contrib.gis import admin
from .models import Shop, ruang

admin.site.register(Shop, admin.GeoModelAdmin)
admin.site.register(ruang, admin.GeoModelAdmin)