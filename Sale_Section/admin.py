from django.contrib import admin

# Register your models here.
from .models import Sale_Section


class Sale_SectionAdmin(admin.ModelAdmin):
    list_display = ('title','heading','description','link_button_name','button_link','image')

admin.site.register(Sale_Section , Sale_SectionAdmin)