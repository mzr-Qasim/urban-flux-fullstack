from django.contrib import admin
from .models import Category

# Register your models here.
class Category_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

    list_display = ('category_name', 'slug', 'cat_image', 'cat_half_col_name', 'cat_image_half_col', 'category_col_height')

admin.site.register(Category, Category_Admin)