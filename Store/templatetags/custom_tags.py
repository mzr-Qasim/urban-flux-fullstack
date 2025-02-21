from django import template

register = template.Library()

@register.simple_tag
def calculate_discount_price(price, sale):
    """Calculate the discounted price based on the original price and sale percentage."""
    try:
        price = float(price)  # Convert price to float
        sale = float(sale)    # Convert sale to float
        if price is not None and sale is not None:
            return price * (1 - sale / 100)  # Calculate discounted price
    except (ValueError, TypeError):
        pass  # If conversion fails, return the original price
    return price  # If there's no sale or conversion fails, return the original price