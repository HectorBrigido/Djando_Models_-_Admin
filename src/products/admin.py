from django.contrib import admin

from .models import Product, DigitalProduct


# Register your models here.
admin.site.register(Product)
admin.site.register(DigitalProduct)