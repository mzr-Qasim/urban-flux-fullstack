from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.simple_tag
def calculate_discount_price(price, sale):
    try:
        price = float(price)  # Convert price to float
        sale = float(sale)    # Convert sale to float
        if price is not None and sale is not None:
            discounted_price = price * (1 - sale / 100)  # Calculate discounted price
            return floatformat(discounted_price, 2)
    except (ValueError, TypeError):
        pass  # If conversion fails, return the original price
    return price  # If there's no sale or conversion fails, return the original price












# cart = Cart(request)
    
#     # Convert cart.session.values() to a list for easier inspection
#     items = list(cart.session.values())
    
#     # Initialize variables to store the total discounted price
#     total_discounted_price = 0
    
#     # Iterate over all items in the cart
#     for item in items:
#         # Check if the item is a dictionary
#         if isinstance(item, dict):
#             # Iterate over the nested dictionaries inside the item
#             for product_key, product_details in item.items():
#                 # Fetch price, sale, and quantity values
#                 price = product_details.get('price')
#                 sale = product_details.get('sale')
#                 quantity = product_details.get('quantity')
                
#                 # Convert price, sale, and quantity to integers (if they exist)
#                 if price is not None:
#                     price = int(price)
#                 if sale is not None:
#                     sale = int(sale)
#                 if quantity is not None:
#                     quantity = int(quantity)
                
#                 # Calculate discounted_price for the current product
#                 if price is not None and sale is not None and quantity is not None:
#                     discounted_price =  price * (1 - sale / 100) * quantity
#                     total_discounted_price += discounted_price