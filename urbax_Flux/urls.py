"""
URL configuration for urbax_Flux project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import toggle_wishlist, wishlist_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search-resuts/', views.search_results, name='search-results'),  
    path('shop/', views.shop, name='shop'), 
    path('product-detail/<id>', views.product_detail, name='product-detail'), 
    path('category/', views.product_category, name='category'), 
    path('category/<int:category>', views.product_category, name='category'), 
    path('contact-us', views.contact_us, name='contact-us'), 
    path('login/', views.loginpage, name='login'), 
    path('login-user/', views.loginUser, name='login-user'), 
    path('logout-user/', views.logoutUser, name='logout-user'),
    path('register/', views.sign_up, name='sign-up'), 
    path('register-user', views.registerUser, name='register-user'), 
    # path('wishlist/', views.wish_list, name='wishlist'), 
    path('toggle-wishlist/<int:product_id>/', toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('cart/', views.shopping_cart, name='Shopping-cart'), 
    path('checkout/', views.checkout, name='checkout'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











