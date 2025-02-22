from django.contrib import admin

# Register your models here.
from .models import Store

class Store_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name','price' ,'product_type','description','Color_1','Color_2','Color_3','Feature_1','Feature_2','Feature_3','Size_1','Size_2','Size_3','Materials_Care_1','Materials_Care_2','Materials_Care_3','stock','category','sale','is_available','Image','product_image_1','product_image_2','product_image_3')

admin.site.register(Store, Store_Admin)



