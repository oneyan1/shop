from django.contrib import admin
from django.urls import path
from category.views import ProdList, ProdDetail

app_name = 'category'

urlpatterns = [
    path('', ProdList, name='ProductList'),
    path('<str:category_slug>/', ProdList, name='ProductListByCategory'),
    path('<int:id>/<str:slug>/', ProdDetail, name='ProductDetails')
]
