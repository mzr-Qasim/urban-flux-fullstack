from django.contrib import admin

# Register your models here.
from .models import Our_Locations


class  Our_LocationsAdmin(admin.ModelAdmin):

    list_display = ('location_city','location','email','phone','timings','close_detail','Image')

admin.site.register(Our_Locations,Our_LocationsAdmin)
