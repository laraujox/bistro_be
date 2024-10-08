from django.contrib.sessions.models import Session

from menu.models import Product
from order.models import Order, OrderItem


class OrderItemRepository:
    def __init__(self):
        self.model = OrderItem

    def create(self, order: Order, product: Product, quantity: int) -> None:
        self.model.objects.create(order=order, product=product, quantity=quantity)

    def get(self, order_id: int) -> [OrderItem]:
        order_items = self.model.objects.filter(order_id=order_id)
        return order_items


class OrderRepository:
    def __init__(self):
        self.model = Order

    def create(self, table_id: str) -> None:
        self.model.objects.create(table_id=table_id)

    def get(self, order_id: int) -> [Order]:
        order_items = self.model.objects.get(id=order_id)
        return order_items

    def update_status(self, order_id: int, status: Order.OrderStatus):
        order = self.get(order_id)
        if order:
            order.status = status
            order.save()
            print("Order updated successfully.")
        else:
            print("Order not found.")
