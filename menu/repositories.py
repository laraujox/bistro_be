from menu.models import OrderItem, Product, Order


class OrderItemRepository:
    def __init__(self):
        self.model = OrderItem

    def create(self, order: Order, product: Product, quantity: int) -> None:
        self.model.objects.create(order=order, product=product, quantity=quantity)
