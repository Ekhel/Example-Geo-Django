from django.contrib.gis import admin

from .models import koordinat, polygon

class PageKoordinat(admin.ModelAdmin):
    list_display = ('nama','keterangan')
    list_display_links = ('nama','keterangan')
    search_fields = ('nama','keterangan')
    list_per_page = 10


class PagePolygon(admin.ModelAdmin):
    list_display = ('nama','keterangan')
    list_display_links = ('nama','keterangan')
    search_fields = ('nama','keterangan')
    list_per_page = 10

admin.site.register(polygon, PagePolygon)
admin.site.register(koordinat, PageKoordinat)