from django.contrib import admin

# Register your models here.

from .models import Site_Settings


class Site_SettingsAdmin(admin.ModelAdmin):
    list_display = ('estimated_delivery','return_time','site_logo','theme_hero_section','tax_rate','product_policies')

admin.site.register(Site_Settings, Site_SettingsAdmin)