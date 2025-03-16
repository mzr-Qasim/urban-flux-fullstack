from django.contrib import admin
from users.models import userProfiles

# Register your models here.


class userprofilesAdmin(admin.ModelAdmin):
    list_display = ["user","first_name","last_name","country","street_address","optional_address","city","state","email","zip_code","phone","order_notes"]

admin.site.register(userProfiles, userprofilesAdmin)