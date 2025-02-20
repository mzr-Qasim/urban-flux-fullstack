from django.contrib import admin
from .models import Cloth_Class

# Register your models here.

class Cloth_ClassAdmin(admin.ModelAdmin):
    list_display = ('cloth_class_name', 'cloth_class_info','cloth_class_link_name','image')

admin.site.register(Cloth_Class,Cloth_ClassAdmin)