from django.shortcuts import render,  get_object_or_404
from Site_Settings.models import Site_Settings
from Hero_Slider.models import Hero_Slider
from Category.models import Category
from Store.models import Store
from Sale_Section.models import Sale_Section
from Cloth_Class.models import Cloth_Class
from Our_Locations.models import Our_Locations

def home(request):
    site_settings = Site_Settings.objects.all()
    hero_slider = Hero_Slider.objects.all()
    categories =  Category.objects.all()
    Products = Store.objects.all()
    sale_section = Sale_Section.objects.all()
    cloth_class_section = Cloth_Class.objects.all()
    our_Stores_section = Our_Locations.objects.all()



    Data = {
        "site_settings_data": site_settings,
        "hero_slider_data": hero_slider,
        "categories_data": categories,
        "sale_section_data" : sale_section,
        "Product_Data" : Products,
        "Cloth_Class_Data": cloth_class_section,
        "Our_Stores_section_data" : our_Stores_section
    }
    return render(request, 'index.html', Data)



def shop(request):
    site_settings = Site_Settings.objects.all()
    Products = Store.objects.all()
    categories =  Category.objects.all()

    Data = {
        "site_settings_data": site_settings,
        "Product_Data" : Products,
        "categories_data": categories,
    }
    return render(request, 'shop.html', Data)






def product_detail(request, id): 
    site_settings = Site_Settings.objects.all()   
    Products = Store.objects.all()
    single_product = Store.objects.get(id__exact=id)
    sale = single_product.sale
    price = single_product.price

    if sale is None:
        discount_price = price
    else: 
        discount_price = price * (1 - sale / 100)
    Data = {
        "site_settings_data": site_settings,
        "product_data" : Products,
        "single_product_data": single_product,
        "current_id": int(id),
        "final_discount_price": discount_price,
    }
    return render(request, 'product-detail.html', Data)


def product_category(request, category):
    categories =  Category.objects.all()
    category_obj = get_object_or_404(Category, id=category)
    product_by_cat = Store.objects.filter( category_id=category)
    site_settings = Site_Settings.objects.all()
    
    Data = {
        "site_settings_data": site_settings,
        "categories_data": categories,
        "cat_obj" : category_obj,
        "product_by_cat_data" : product_by_cat 
    }
    return render(request, 'category.html' , Data)


def login(request):
    site_settings = Site_Settings.objects.all()
    Data = {
        "site_settings_data": site_settings,
    }
    return render(request, 'login.html', Data)

def sign_up(request):  
    site_settings = Site_Settings.objects.all()
 
    Data = {
        "site_settings_data": site_settings,
    }
    return render(request, 'sign-up.html', Data)


def wish_list(request):
    site_settings = Site_Settings.objects.all()

    Data = {
        "site_settings_data": site_settings,
    }
    return render(request, 'wishlist.html' , Data)


def shopping_cart(request):
    site_settings = Site_Settings.objects.all()
    current_url_name = request.resolver_match.url_name.replace('-',' ')

    Data = {
        "site_settings_data": site_settings,
        "url_name" : current_url_name
    }
    return render(request, 'shopping-cart.html', Data)


def checkout(request):
    site_settings = Site_Settings.objects.all()
    Data = {
        "site_settings_data": site_settings,
    }
    return render(request, 'checkout.html', Data)