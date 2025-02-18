from django.shortcuts import render
from Hero_Slider.models import Hero_Slider
from Category.models import Category
from Store.models import Store
from Sale_Section.models import Sale_Section

def home(request):
    hero_slider = Hero_Slider.objects.all()
    categories =  Category.objects.all()
    Products = Store.objects.all()
    sale_section = Sale_Section.objects.all()



    Data = {
        "hero_slider_data": hero_slider,
        "categories_data": categories,
        "Product_Data" : Products,
        "sale_section_data" : sale_section,
    }
    return render(request, 'index.html', Data)






def shop(request):
    Products = Store.objects.all()
    categories =  Category.objects.all()

    Data = {
        "Product_Data" : Products,
        "categories_data": categories,
    }
    return render(request, 'shop.html', Data)





def product_detail(request):
    return render(request, 'product-detail.html')


def product_category(request):
    return render(request, 'category.html')


def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign-up.html')


def wish_list(request):
    return render(request, 'wishlist.html')


def shopping_cart(request):
    return render(request, 'shopping-cart.html')


def checkout(request):
    return render(request, 'checkout.html')