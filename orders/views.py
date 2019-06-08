from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def AdminOrderDetail(request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'admin/orders/order/detail.html', {'order':order})


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
                order = form.save(commit = False)
                if cart.cupon:
                        order.cupon = cart.cupon
                        order.discount = cart.cupon.discount
                order.save()
                for item in cart:
                        OrderItem.objects.create(order=order, product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
                cart.clear()
                send_mail('Nowe zamówienie', 'Nowe zamówienie dodane do admin panelu', 
                        'sklepszkielety@gmail.com', ['yangrodno@yandex.ru'], fail_silently=False)
                return render(request, 'orders/order/created.html', {'order':order})
    
    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form':form})

