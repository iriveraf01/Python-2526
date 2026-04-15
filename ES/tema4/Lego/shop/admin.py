from django.contrib import admin
from .models import Profile, Category, Product
# Registro sencillo (aparecen tal cual)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)