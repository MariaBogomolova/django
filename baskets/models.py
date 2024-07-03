from django.db import models
from users.models import User
from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self, request):
        total_q = 0
        list_of_baskets = self.objects.filter(user=request.user)
        for basket in list_of_baskets:
            total_q += basket.quantity
        return total_q

    def total_sum(self, request):
        total_cost = 0
        list_of_baskets = self.objects.filter(user=request.user)
        for basket in list_of_baskets:
            total_cost += basket.quantity * basket.product.price
        return total_cost
