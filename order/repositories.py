from menu.models import Product
from order.models import Order, OrderItem


class OrderItemRepository:
    def __init__(self):
        self.model = OrderItem

    def create(self, order: Order, product: Product, quantity: int) -> None:
        self.model.objects.create(order=order, product=product, quantity=quantity)
