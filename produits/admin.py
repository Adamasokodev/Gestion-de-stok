from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'unit_price', 'stock', 'created_at')
    search_fields = ('sku', 'name')
