from django.contrib import admin

from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_filter=["item","sold_by","date_sold"]
    list_display=["item","quantity","date_sold"]

admin.site.register(Cart)
