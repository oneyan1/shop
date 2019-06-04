from django.urls import path
from .views import OrderCreate

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreate, name='OrderCreate')
]
