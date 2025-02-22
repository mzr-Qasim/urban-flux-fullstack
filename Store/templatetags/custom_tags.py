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