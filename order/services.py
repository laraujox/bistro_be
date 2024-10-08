from order.constants import ORDER_FLOW
from order.models import Order


class OrderService:
    order_flow_size = len(ORDER_FLOW)

    @staticmethod
    def get_downgraded_status(current_status: Order.OrderStatus) -> Order.OrderStatus:
        downgraded_status_index = ORDER_FLOW.index(current_status) - 1
        if downgraded_status_index >= 0:
            return ORDER_FLOW[downgraded_status_index]
        return current_status

    def get_upgraded_status(
            self, current_status: Order.OrderStatus) -> Order.OrderStatus:
        upgraded_status_index = ORDER_FLOW.index(current_status) + 1
        if upgraded_status_index < self.order_flow_size:
            return ORDER_FLOW[upgraded_status_index]
        return current_status
