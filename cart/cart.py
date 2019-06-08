from decimal import Decimal
from django.conf import settings
from category.models import Product
from cupons.models import Cupon

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.cupon_id = self.session.get('cupon_id')
   


    def add(self, product, quantity=1, update_quantity = False):
        product_id = str(product.id)
        if product_id not in self.cart:
           self.cart[product_id] = {'quantity':0,
                                    'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def getTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True 
        
    @property
    def cupon(self):
        if self.cupon_id:
            return Cupon.objects.get(id=self.cupon_id)
        return None

    def getDiscount(self):
        if self.cupon:
            return (self.cupon.discount / Decimal('100')) * self.getTotalPrice()
        return Decimal('0')

    def getTotalPriceAfterDiscount(self):
        return self.getTotalPrice() - self.getDiscount()
