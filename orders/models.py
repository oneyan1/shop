from django.db import models
from category.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name='Imie')
    last_name = models.CharField(max_length=50, verbose_name='Nazwisko')
    email = models.EmailField()
    address = models.CharField(max_length=200, verbose_name='Adres')
    postal_code = models.CharField(max_length=10, verbose_name='Kod pocztowy')
    city = models.CharField(max_length=100, verbose_name='Miasto')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')
    updated = models.DateTimeField(auto_now=True, verbose_name='Data odświeżenia')
    paid = models.BooleanField(default=False, verbose_name='Opłata')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Zamóweinie: {}'.format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=1, verbose_name='Cena')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Ilość')
    
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

