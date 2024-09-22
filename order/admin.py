from django.contrib import admin

from order.models import OrderItem, Order


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