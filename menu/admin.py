from django.contrib import admin

from menu.models import Product, Combo, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at', 'updated_at')
    list_filter = ('available',)
    search_fields = ('name', 'description')


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at', 'updated_at')
    list_filter = ('available',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'created_at', 'updated_at')
    list_filter = ('available',)
    search_fields = ('name', 'available')
