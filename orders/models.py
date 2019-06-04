from django.db import models
from category.models import Product

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(verbose_name='Imię', max_length=50)
    last_name = models.CharField(verbose_name='Nazwisko', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address =  models.CharField(verbose_name='Adres', max_length=250)
    postal_code = models.CharField(verbose_name='Kod potcztowy', max_length=20)
    city = models.CharField(verbose_name='Miasto', max_length=100)
    created = models.DateTimeField(verbose_name='Dodany', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Aktualizacja', auto_now=True)
    paid = models.BooleanField(verbose_name='Opłacony', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Zamówienie'
        verbose_name_plural = 'Zamówienia'

    def __str__(self):
        return 'Zamówienie: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Cena', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Ilosć', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity