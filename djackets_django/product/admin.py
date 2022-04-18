from django.contrib import admin

from .models import Category, Product, Classes, Department

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Classes)