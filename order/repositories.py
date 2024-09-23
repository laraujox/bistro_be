from menu.models import Product
from order.models import Order, OrderItem


class OrderItemRepository:
    def __init__(self):
        self.model = OrderItem

    def create(self, order: Order, product: Product, quantity: int) -> None:
        self.model.objects.create(order=order, product=product, quantity=quantity)

    def get_by_order(self, order_id: int) -> [OrderItem]:
        order_items = self.model.objects.filter(order_id=order_id)
        return order_items
