from django.shortcuts import render

def home(request):
    return render(request, 'index.html')



def shop(request):
    return render(request, 'shop.html')


def shop(request):
    return render(request, 'shop.html')



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