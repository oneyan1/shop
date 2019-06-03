from django.shortcuts import render, get_object_or_404
from . models import Category, Product

from cart.forms import CartAddProductForm

# Strona z listą produktów
def ProdList(requiest, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(requiest,"category/product/list.html", context)

# Strona produktu 
def ProdDetail(requiest, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available = True)
    cart_product_form = CartAddProductForm()
    context = {'product': product,
               'cart_product_form': cart_product_form}
    return render(requiest, "category/product/details.html", context)
