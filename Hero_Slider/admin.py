from django.contrib import admin

# Register your models here.
from .models import Hero_Slider

class HeroSlider_Admin(admin.ModelAdmin):
    list_display = ('title','info','link_name','link','image')


admin.site.register(Hero_Slider, HeroSlider_Admin)