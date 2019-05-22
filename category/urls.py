from django.contrib import admin
from django.urls import path
from . views import ProdList, ProdDetail

urlpatterns = [
    path('', ProdList, name='ProductList'),
    path('<str:category_slug>/', ProdList, name='ProductListByCategory'),
    path('<int:id>/<str:slug>/', ProdDetail, name='ProductDetails')
]
