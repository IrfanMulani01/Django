from django.contrib import admin
from .models import Product

class Disp_prod(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'description']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']

admin.site.register(Product, Disp_prod)