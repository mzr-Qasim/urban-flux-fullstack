from django.db import models

# Create your models here.
from Store.models import Store
from django.contrib.auth.models import User

class wish_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Store, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Ensure a user can't add the same product twice

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.product.product_name}"