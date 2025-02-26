from django.contrib import admin

# Register your models here.
from .models import Locations_map


class Locations_mapAdmin(admin.ModelAdmin):

    list_display = ('location_title','location_map_image','location_svg_code')


admin.site.register(Locations_map, Locations_mapAdmin)