from django.contrib import admin

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'quantity', 'available']
    list_filter = ['available', 'createdDate', 'upgradeDate']
    list_editable = ['price', 'quantity', 'available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)