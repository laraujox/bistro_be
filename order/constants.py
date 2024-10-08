from order.models import Order

ORDER_FLOW = [
    Order.OrderStatus.PENDING,
    Order.OrderStatus.PREPARING,
    Order.OrderStatus.READY,
]
