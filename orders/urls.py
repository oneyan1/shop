from django.urls import path
from .views import OrderCreate, AdminOrderDetail

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreate, name='OrderCreate'),
    path('admin/order/<int:order_id>/', AdminOrderDetail, name='AdminOrderDetail'),
    
]
