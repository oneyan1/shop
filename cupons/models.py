from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='Kod kupona')
    valid_from = models.DateTimeField(verbose_name='Ważność od')
    valid_to = models.DateTimeField(verbose_name='Ważność do')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Zniżka')
    active = models.BooleanField(verbose_name='Wazność')

    def __str__(self):
        return self.code

