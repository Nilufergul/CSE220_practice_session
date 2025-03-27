from django.db import models

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey('products_app.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
