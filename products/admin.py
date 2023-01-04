from django.contrib import admin
from .models import Product, ProductImage


# Admin display
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["name","price","type"]
    list_display = ["name", "price","quantity","minQuantity","created_on"]

class ProductImageAdmin(admin.ModelAdmin):
    list_filter = ["product",]
    list_display = ["id", "product"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)