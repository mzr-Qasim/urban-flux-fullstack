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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import toggle_wishlist, wishlist_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search-resuts/', views.search_results, name='search-results'),  
    path('shop/', views.shop, name='shop'), 
    path('product-detail/<id>', views.product_detail, name='product-detail'), 
    path('category/', views.product_category, name='category'), 
    path('category/<int:category>', views.product_category, name='category'), 
    path('contact-us', views.contact_us, name='contact-us'), 
    path('my-account', views.my_accountpage, name='my-account'), 
    path('login/', views.loginpage, name='login'), 
    path('login-user/', views.loginUser, name='login-user'), 
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # URL when the password reset email is sent
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # URL for the user to confirm and reset their password
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # URL when the password has been successfully reset
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('logout-user/', views.logoutUser, name='logout-user'),
    path('register/', views.sign_up, name='sign-up'), 
    path('register-user', views.registerUser, name='register-user'), 
    path('toggle-wishlist/<int:product_id>/', toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('cart/', views.shopping_cart, name='Shopping-cart'), 
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'), 
    path('process-checkout', views.process_checkout, name= 'process_checkout'),
    path('checkout_session', views.checkout_session, name= 'checkout_session'),
    path('payment-success/', views.successPage, name='success'),
    path('payment-failed/', views.cancelPage, name='cancel'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




