from django.contrib import admin

# Register your models here.
from product_variations.models import product_variations

class product_variationsAdmin(admin.ModelAdmin):
    list_display = ('size','color','feature','material_care','product')

admin.site.register(product_variations,product_variationsAdmin)