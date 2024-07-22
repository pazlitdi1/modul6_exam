from django.contrib import admin
from .models import Category, Shop, Nav_Category, Meat, Bread, Fruits, Vegetables, All_products
from import_export.admin import ImportExportModelAdmin


admin.site.register(Nav_Category)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register([Meat, Bread, Fruits])
admin.site.register([Vegetables, All_products])
