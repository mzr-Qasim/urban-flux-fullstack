from django.shortcuts import redirect, render,  get_object_or_404
from django.core.paginator import Paginator
from Site_Settings.models import Site_Settings
from Hero_Slider.models import Hero_Slider
from Category.models import Category
from Store.models import Store
from Sale_Section.models import Sale_Section
from Our_Locations.models import Our_Locations
from Locations_map.models import Locations_map
from orders.models import orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from wish_list.models import wish_list
from product_variations.models import product_variations
from django.http import HttpResponseRedirect
from cart.cart import Cart
from django.template.defaultfilters import floatformat
from django.db.models import Q
from users.models import userProfiles
import stripe
from django.conf import settings

from django.http import JsonResponse

def home(request):
    site_settings = Site_Settings.objects.all()
    hero_slider = Hero_Slider.objects.all()
    categories =  Category.objects.all()
    products = reversed(Store.objects.all())
    best_seller = reversed(Store.objects.all())
    sale_section = Sale_Section.objects.all()
    our_Stores_section = Our_Locations.objects.all()
    if request.user.is_authenticated:
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0      
    



    Data = {
        "site_settings_data": site_settings,
        "wishlist_count" : wishlist_count,
        "hero_slider_data": hero_slider,
        "categories_data": categories,
        "sale_section_data" : sale_section,
        "product_Data" : products,
        "best_seller_Data" : best_seller,
        "Our_Stores_section_data" : our_Stores_section,
        
        
    }
    return render(request, 'index.html', Data)





def search_results(request):
    site_settings = Site_Settings.objects.all()
    categories =  Category.objects.all()
    products = reversed(Store.objects.all())
    searchTerm = request.GET.get('Search', '').strip()
    if searchTerm == '':
        return redirect('/')
    if len(searchTerm) == 1:
        error_result = 0
    else:
        error_result = ""

    cleaned_searchTerm = ' '.join(searchTerm.split())
    search_product = Store.objects.filter(
    Q(name__icontains=cleaned_searchTerm) | Q(category__category_name__contains=cleaned_searchTerm)
)
    
    search_product_count = search_product.count()
    if request.user.is_authenticated:
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0
    Data = {
        "site_settings_data": site_settings,
        "wishlist_count" : wishlist_count,
        "product_Data" : products,
        "categories_data": categories,
        "SearchTerm" : searchTerm,
        "Search_products": search_product,
        "search_product_count_data" : search_product_count,
        "error_result": error_result,

    }
    return render (request, 'search_results.html', Data)





def shop(request):
    site_settings = Site_Settings.objects.all()
    products = reversed(Store.objects.all())
    Products = Store.objects.all()
    product_data = Products.count()
    products_limit = 8
    Products = Paginator(Products, products_limit)
    page = request.GET.get("page")
    page_obj = Products.get_page(page)
    page_obj_count =  [x+1 for x in range(Products.num_pages)]
    categories =  Category.objects.all()
    if request.user.is_authenticated:
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0

    Data = {
        "site_settings_data": site_settings,
        "wishlist_count" : wishlist_count,
        "product_Data" : products,
        "categories_data": categories,
        "product_data" : product_data,
        "Product_Data" : Products,
        "products_show_data" : products_limit,
        "products_per_page" : page_obj,
        "page_obj_count" : page_obj_count,
    }
    return render(request, 'shop.html', Data)





def product_detail(request, id): 
    site_settings = Site_Settings.objects.all()   
    categories =  Category.objects.all()
    products = reversed(Store.objects.all())
    Products = Store.objects.all()
    single_product = Store.objects.get(id__exact=id)
    product_variation = product_variations.objects.filter(product=single_product)
    if request.user.is_authenticated:
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0

    Data = {
        "site_settings_data": site_settings,
        "categories_data": categories,
        "product_Data" : products,
        "wishlist_count" : wishlist_count,
        "product_data" : Products,
        "single_product_data": single_product,
        "current_id": int(id),
        "product_variations_data" : product_variation,
    }
    return render(request, 'product-detail.html', Data)


def product_category(request, category):
    categories =  Category.objects.all()
    category_obj = get_object_or_404(Category, id=category)
    products = reversed(Store.objects.all())
    product_by_cat = Store.objects.filter( category_id=category)
    site_settings = Site_Settings.objects.all()
    if request.user.is_authenticated:
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0
    
    
    Data = {
        "site_settings_data": site_settings,
        "wishlist_count" : wishlist_count,
        "product_Data" : products,
        "categories_data": categories,
        "cat_obj" : category_obj,
        "product_by_cat_data" : product_by_cat 
    }
    return render(request, 'category.html' , Data)



def contact_us(request):
    site_settings = Site_Settings.objects.all()  
    categories =  Category.objects.all()
    products = reversed(Store.objects.all())
    our_Stores_section = Our_Locations.objects.all()
    locations_map_section = Locations_map.objects.all()
    if request.user.is_authenticated:
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0



    Data = {
        "site_settings_data": site_settings,
        "wishlist_count" : wishlist_count,
        "product_Data" : products,
        "Our_Stores_section_data" : our_Stores_section,
        "locations_map_data" : locations_map_section,
        "categories_data": categories,
    } 
    return render(request, 'contact-us.html', Data)





def loginpage(request):
    if request.user.is_authenticated:
        return redirect('my-account') 
    else:
        site_settings = Site_Settings.objects.all()
        categories =  Category.objects.all()
        products = reversed(Store.objects.all())


        Data = {
            "site_settings_data": site_settings,
            "categories_data": categories,
            "product_Data" : products,
        }
        return render(request, 'login.html', Data)

def sign_up(request):  
    if request.user.is_authenticated:
        return redirect('my-account') 
    else:
        site_settings = Site_Settings.objects.all()
        categories =  Category.objects.all()
        products = reversed(Store.objects.all())
    
        Data = {
            "site_settings_data": site_settings,
            "categories_data": categories,
            "product_Data" : products,
        }
        return render(request, 'sign-up.html', Data)

def my_accountpage(request):
    if request.user.is_authenticated:
        site_settings = Site_Settings.objects.all()
        categories =  Category.objects.all()
        products = reversed(Store.objects.all())
        wishlist_count = wish_list.objects.filter(user=request.user).count()
    

        Data = {
        "site_settings_data": site_settings,
        "categories_data": categories,
        "product_Data" : products,
        "wishlist_count" : wishlist_count,
    }
        return render(request, "my-account.html", Data)
    else:
        return redirect('login')
    

# def lostPassword(request):
#     if request.user.is_authenticated:
#         return redirect('my-account')
#     else:
#         site_settings = Site_Settings.objects.all()
#         categories =  Category.objects.all()
#         products = reversed(Store.objects.all())


#         Data = {
#         "site_settings_data": site_settings,
#         "categories_data": categories,
#         "product_Data" : products,
#         }
#         return render (request, "lost-password.html", Data)



def registerUser(request):
    r_fname = request.POST['first_name']
    r_lname = request.POST['last_name']
    r_username = request.POST['username']
    r_email = request.POST['email']
    r_password = request.POST['password'] 
    r_rpassword = request.POST['rpassword']

    if r_fname == '' or r_lname == '' or r_username == '' or r_email == '' or r_password == '' or r_rpassword == '':
        messages.warning(request, "Please fill all fields")

    elif len(r_password) < 8 :
            messages.warning(request, "Password too short")
    elif r_password != r_rpassword :
            messages.warning(request, "Passwords do not match")
    else:
        user = User.objects.create_user(first_name = r_fname, last_name = r_lname ,username = r_username, email = r_email, password = r_password)
        messages.success(request, "Account created successfully")
        return redirect('login')
    
    site_settings = Site_Settings.objects.all()
    categories =  Category.objects.all()
    Data = {
        "site_settings_data": site_settings,
        "categories_data": categories,
    }

   
    return render(request, 'sign-up.html', Data)




def loginUser(request):
    r_username = request.POST['username']
    r_password = request.POST['password'] 
    if r_username == '' or r_password == '':
        messages.warning(request, "Please provide a username and password")
        return redirect('login')
    user = authenticate(request, username=r_username, password=r_password)
    if user is not None:
        login(request, user)
        request.session['first_name'] = user.first_name
        return redirect('my-account')
    else:
        messages.warning(request, "User does not exist.")
    site_settings = Site_Settings.objects.all()
    categories =  Category.objects.all()
    Data = {
        "site_settings_data": site_settings,
        "categories_data": categories,
    }
    return render(request, 'login.html', Data)

def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')





def shopping_cart(request):
    if request.user.is_authenticated:
        site_settings = Site_Settings.objects.all()
        products = reversed(Store.objects.all())
        current_url_name = request.resolver_match.url_name.replace('-',' ')
        if request.user.is_authenticated:
            wishlist_count = wish_list.objects.filter(user=request.user).count()
        else:
            wishlist_count = 0
        categories =  Category.objects.all()


        cart = Cart(request)

        # Convert cart.session.values() to a list for easier inspection
        items = list(cart.session.values())

        # Initialize variables to store the total discounted price
        total_discounted_price = 0

        # Iterate over all items in the cart
        for item in items:
            # Check if the item is a dictionary
            if isinstance(item, dict):
                # Iterate over the nested dictionaries inside the item
                for product_key, product_details in item.items():
                    # Fetch price, sale, and quantity values
                    price = product_details.get('price')
                    sale = product_details.get('sale')
                    quantity = product_details.get('quantity')

                    # Convert price, sale, and quantity to integers (if they exist)
                    if price is not None:
                        price = int(price)
                    if sale is not None:
                        sale = int(sale)
                    if quantity is not None:
                        quantity = int(quantity)

                    # Calculate discounted_price for the current product
                    if price is not None and sale is not None and quantity is not None:
                        discounted_price =  price * (1 - sale / 100) * quantity
                        total_discounted_price += discounted_price
                    else:
                        discounted_price = price * (1 - (sale if sale is not None else 0) / 100) * quantity

        try:
            for tax in site_settings:
                tax_value = tax.tax_rate  
            tax_price = tax_value * total_discounted_price / 100
            final_price = tax_price + total_discounted_price
        except:
            pass

        Data = {
            "site_settings_data": site_settings,
            "categories_data": categories,
            "product_Data" : products,
            "wishlist_count" : wishlist_count,
            "url_name" : current_url_name,
            "total_discounted_price" : total_discounted_price,
            "tax_value_price" : tax_price,
            "final_price" : final_price,
        }
        return render(request, 'shopping-cart.html', Data)
    else:
        return redirect('login')


def checkout(request):
    if request.user.is_authenticated:

        site_settings = Site_Settings.objects.all()
        categories =  Category.objects.all()
        products = reversed(Store.objects.all())

        if request.user.is_authenticated:
            wishlist_count = wish_list.objects.filter(user=request.user).count()
        else:
            wishlist_count = 0

        cart = request.session.get('cart', {})

        if len(cart) == 0:
            return redirect('Shopping-cart')


        cart = Cart(request)

        # Convert cart.session.values() to a list for easier inspection
        items = list(cart.session.values())

        # Initialize variables to store the total discounted price
        total_discounted_price = 0

        # Iterate over all items in the cart
        for item in items:
            # Check if the item is a dictionary
            if isinstance(item, dict):
                # Iterate over the nested dictionaries inside the item
                for product_key, product_details in item.items():
                    # Fetch price, sale, and quantity values
                    price = product_details.get('price')
                    sale = product_details.get('sale')
                    quantity = product_details.get('quantity')

                    # Convert price, sale, and quantity to integers (if they exist)
                    if price is not None:
                        price = int(price)
                    if sale is not None:
                        sale = int(sale)
                    if quantity is not None:
                        quantity = int(quantity)

                    # Calculate discounted_price for the current product
                    if price is not None and sale is not None and quantity is not None:
                        discounted_price =  price * (1 - sale / 100) * quantity
                        total_discounted_price += discounted_price
                    else:
                        discounted_price = price * (1 - (sale if sale is not None else 0) / 100) * quantity

        try:
            for tax in site_settings:
                tax_value = tax.tax_rate  
            tax_price = tax_value * total_discounted_price / 100
            final_price = tax_price + total_discounted_price
        except:
            pass


        Data = {
            "site_settings_data": site_settings,
            "categories_data": categories,
             "product_Data" : products,
            "wishlist_count" : wishlist_count,
            "total_discounted_price" : total_discounted_price,
            "tax_value_price" : tax_price,
            "final_price" : final_price,
        }
        return render(request, 'checkout.html', Data)
    else:
        return redirect('login')




def process_checkout(request):

        if request.method == 'POST':
            user = request.user

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            street_address = request.POST.get('street_address')
            optional_address = request.POST.get('optional_address', '').strip()
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            order_notes = request.POST.get('order_notes')





            user.first_name = first_name
            user.last_name =  last_name
            user.country = country
            user.street_address = street_address


            if optional_address:
                user.optional_address = optional_address
            user.city = city
            user.state = state
            user.zip_code = zip_code
            user.phone = phone
            user.email = email
            if order_notes: 
                user.order_notes = order_notes

            user.save()


            profile, created = userProfiles.objects.get_or_create(user=user)
            profile.first_name = country
            profile.last_name = country
            profile.country = country
            profile.street_address = street_address
            profile.optional_address = optional_address
            profile.city = city
            profile.state = state
            profile.zip_code = zip_code
            profile.phone = phone
            profile.email = email
            profile.order_notes = order_notes
            profile.save()


            if first_name == ''  or last_name == '' or country == '' or street_address == '' or  city == '' or state == '' or zip_code == '' or phone == '' or  email == '':
                messages.warning(request, "Please fill all fields")
                return redirect ('checkout')

            else:
                return redirect ('checkout_session')




   

def checkout_session(request):
    site_settings = Site_Settings.objects.all()
    for site in site_settings:
        final_tax = site.tax_rate
    cart = Cart(request)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Retrieve cart items
    items = list(cart.session.values())[4]  # Access the product details at index 4
    print(items)  # Debugging: Print the structure of `items`

    # Ensure `items` is a list of dictionaries
    if not isinstance(items, list):
        items = [items]  # Convert to a list if it's a single dictionary

    # Validate cart data and calculate base_amount
    try:
        base_amount = 0
        for item in items:
            # Check if the item is a dictionary
            if isinstance(item, dict):
                # Iterate over the nested dictionaries inside the item
                for product_key, product_details in item.items():
                    # Fetch price, quantity, name, and image values
                    price = product_details.get('price')
                    quantity = product_details.get('quantity')
                    name = product_details.get('name')
                    image = product_details.get('image')

                    # Debugging: Print the fetched values
                    print(f"Price: {price}, Quantity: {quantity}, Name: {name}, Image: {image}")

                    # Validate and calculate base_amount
                    if price is not None and quantity is not None:
                        try:
                            price = float(price)  # Convert price to float
                            quantity = int(quantity)  # Convert quantity to int
                            base_amount += price * quantity
                        except (ValueError, TypeError) as e:
                            raise ValueError(f"Invalid 'price' or 'quantity' value: {e}")
                    else:
                        raise ValueError("Missing 'price' or 'quantity' in product details")
            else:
                raise ValueError("Invalid item format: expected a dictionary")
    except ValueError as e:
        print(f"Error processing cart data: {e}")
        return JsonResponse({'error': 'Invalid cart data'}, status=400)

    tax_rate = 0.10

    aftertax = base_amount + (base_amount * final_tax)  # Total amount after tax

    try:
        # Create line items for Stripe checkout
        line_items = []
        for item in items:
            if isinstance(item, dict):
                for product_key, product_details in item.items():
                    price = product_details.get('price')
                    quantity = product_details.get('quantity')
                    name = product_details.get('name')
                    image = product_details.get('image')

                    if price is not None and quantity is not None:
                        # Construct the full image URL
                        image_url = request.build_absolute_uri(settings.MEDIA_URL + image)


                        line_items.append({
                            'price_data': {
                                'currency': 'usd',
                                'product_data': {
                                    'name': name,  # Use the product name

                                    'images': [image_url],  # Use the full image URL
                                },
                                'unit_amount': int(float(price) * 100),  # Convert to paisa
                            },
                            'quantity': int(quantity),  # Ensure quantity is an integer
                       
                        })

        # Add the tax as a separate line item
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Tax (10%)',
                },
                'unit_amount': int(final_tax * aftertax / 100),  # Convert to paisa
                # tax_price = tax_value * total_discounted_price / 100

            },
            'quantity': 1,
        })


        # Create the Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url='http://127.0.0.1:8000/payment-success',
            cancel_url='http://127.0.0.1:8000/payment-failed/',
        )

        # Create an order in the database
        order = orders.objects.create(
            user=request.user,
            total_price=aftertax / 100,  # Convert cents back to PKR
            payment_status="unpaid",
        )

        # Redirect to the Stripe checkout page
        return redirect(checkout_session.url, code=303)

    except Exception as e:
        print(f"Error: {e}")  # Debugging: Print the error message
        return JsonResponse({'error': str(e)}, status=400)





def successPage(request):
    return render (request, 'success.html')



def cancelPage(request):
    return render (request, 'cancel.html')






def wishlist_view(request):
    if request.user.is_authenticated:
        site_settings = Site_Settings.objects.all()
        categories =  Category.objects.all()
        products = reversed(Store.objects.all())
        wishlist_items = wish_list.objects.filter(user=request.user)
        if request.user.is_authenticated:
            wishlist_count = wish_list.objects.filter(user=request.user).count()
        else:
            wishlist_count = 0
        Data = {
            "site_settings_data": site_settings,
            "wishlist_items" : wishlist_items,
            "product_Data" : products,
            "wishlist_count" : wishlist_count,
            "categories_data": categories,
        }
        return render(request, 'wishlist.html', Data)
    else:
        return redirect('login')


def toggle_wishlist(request, product_id):
    product = get_object_or_404(Store, id=product_id)
    wishlist_item, created = wish_list.objects.get_or_create(user=request.user, product=product)
    
    if not created: 
        wishlist_item.delete()
        messages.warning(request, f"'{product.name}' has been removed from your wishlist.")
    
    # Redirect back to the page the user was on
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




def cart_add(request, id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Store, id=id)
        
        
        selected_size = request.POST.get('size')
        selected_color = request.POST.get('color')
        
        

        cart.add(
            product=product,
            size=selected_size,  
            color=selected_color  
        )
    
    
    return redirect('Shopping-cart')







def item_clear(request, id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Store, id=id)

        selected_size = request.POST.get('size')
        selected_color = request.POST.get('color')



        cart.remove(
                product=product,
                size=selected_size,  
                color=selected_color  
            )
    


    return redirect("Shopping-cart")





def item_increment(request, id):

    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Store, id=id)
        
        
        selected_size = request.POST.get('size')
        selected_color = request.POST.get('color')
        
        

        cart.add(
            product=product,
            size=selected_size,  
            color=selected_color  
        )
    return redirect("Shopping-cart")



def item_decrement(request, id):
    cart = Cart(request)
    product = get_object_or_404(Store, id=id)      
    selected_size = request.POST.get('size')
    selected_color = request.POST.get('color')

    cart.decrement(
            product=product,
            size=selected_size,  
            color=selected_color  
        )
    return redirect("Shopping-cart")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("Shopping-cart")



def cart_detail(request):

    return render(request, 'checkout.html')


