from django.shortcuts import render, get_object_or_404
from Store.models import Store
from Category.models import Category
from Site_Settings.models import Site_Settings
# Create your views here.

# def shop(request, category_slug = None):
#     site_settings = Site_Settings.objects.all()
#     categories = None
#     Products = None
#     if category_slug != None:
#         categories = get_object_or_404(Category, slug = category_slug)
#         Products = Store.objects.filter(category = categories, is_available = True)

#     else:
#         Products = Store.objects.all().filter(is_available = True)

#     Data = {
#         "Product_data" : Products,
#         "site_settings_data": site_settings
#     }

#     return render(request, 'shop.html', Data)


# def product_detail(request, category_slug, product_slug): 
#     try:
#         single_product = Store.objects.get(category_slug = category_slug, slug  = product_slug)
#     except Exception as e:
#         raise e
    
#     Data = {
#         "single_product_data" : single_product
#     }
#     return render(request, 'product-detail.html', Data)