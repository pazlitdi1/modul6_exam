from django.contrib import admin
from .models import Category, Shop, Nav_Category, Meat, Bread, Fruits, Vegetables, All_products
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Nav_Category)
# admin.site.register(Shop)
# admin.site.register(Category)
# admin.site.register([Meat, Bread, Fruits])
# admin.site.register([Vegetables, All_products])

@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug',)
    list_display_links = ('title', 'price',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'rating', 'created',)
    list_display_links = ('title', 'price', 'slug', 'rating', )
    search_fields = ('title',)


@admin.register(Nav_Category)
class Nav_CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'created',)
    list_display_links = ('title', 'price', 'slug', 'created',)
    search_fields = ('title',)


@admin.register(Meat)
class MeatAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'created','description')
    list_display_links = ('title', 'price', 'slug', 'created', 'description')
    search_fields = ('title',)


@admin.register(Bread)
class BreadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'created', 'description')
    list_display_links = ('title', 'price', 'slug', 'created', 'description')
    search_fields = ('title',)


@admin.register(Fruits)
class FruitsdAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'created', 'description')
    list_display_links = ('title', 'price', 'slug', 'created', 'description')
    search_fields = ('title',)


@admin.register(Vegetables)
class VegetablesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'created', 'description')
    list_display_links = ('title', 'price', 'slug', 'created', 'description')
    search_fields = ('title',)


@admin.register(All_products)
class All_productsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'slug', 'created', 'description')
    list_display_links = ('title', 'price', 'slug', 'created', 'description')
    search_fields = ('title',)
