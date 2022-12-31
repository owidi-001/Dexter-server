from django.contrib import admin
from .models import Product


# Admin display
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["name","price","type"]
    list_display = ["name", "price","quantity","minQuantity","created_on"]

admin.site.register(Product, ProductAdmin)