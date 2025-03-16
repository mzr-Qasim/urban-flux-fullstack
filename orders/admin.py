from django.contrib import admin

# Register your models here.
from .models import orders , orderitem

class ordersAdmin(admin.ModelAdmin):
    list_display =  ['user','created_at','updated_at','status','payment_status','payment_id','total_price']

admin.site.register(orders, ordersAdmin)


class orderitemAdmin(admin.ModelAdmin):
    list_display =  ['order','product_name','quantity','price']

admin.site.register(orderitem, orderitemAdmin)