from django.contrib import admin

# Register your models here.
from .models import Store

class Store_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','price' ,'product_type','description','stock','category','sale','is_available','image','product_image_1','product_image_2','product_image_3')

admin.site.register(Store, Store_Admin)



