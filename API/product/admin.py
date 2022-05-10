from django.contrib import admin

from .models import Category, Product, Classes, Department, Student, Program

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Classes)
admin.site.register(Student)
admin.site.register(Program)