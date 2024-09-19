from django.contrib import admin

from menu.models import Product, Combo, Category, Order, OrderItem


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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Removes extra empty fields for new OrderItems
    fields = ['product', 'quantity']
    autocomplete_fields = ['product']  # Enable autocomplete if you have many products


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)
    inlines = [OrderItemInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('items__product')

    def order_items(self, obj):
        return ", ".join([f"{item.quantity} x {item.product.name}" for item in obj.items.all()])

    order_items.short_description = 'Order Items'