from django.contrib import admin
from .models import Profile, Category, Product, Order, OrderItem
# Registro sencillo (aparecen tal cual)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)