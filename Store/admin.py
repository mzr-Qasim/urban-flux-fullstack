from django.contrib import admin

# Register your models here.
from .models import Store

class Store_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name','price' ,'product_type','description','stock','category','sale','is_available','Image','product_image_1','product_image_2','product_image_3')

admin.site.register(Store, Store_Admin)



