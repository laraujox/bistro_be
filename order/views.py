import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from menu.models import Product
from order.models import Order
from order.repositories import OrderItemRepository, OrderRepository
from order.services import OrderService

order_item_repository = OrderItemRepository()
order_repository = OrderRepository()
order_service = OrderService()


@method_decorator(csrf_exempt, name='dispatch')
class CreateOrderView(View):
    def post(self, request, *args, **kwargs):
        """Handle the creation of a new order from a POST request.

        This view processes a POST request containing a list of items to be ordered.
        It creates a new order, retrieves the corresponding products, and associates
        them with the order by adding them to the order using the `OrderItemRepository`.

        Args:
            request (WSGIRequest): The HTTP request object. Must be a POST request with a JSON body.

        Request body:
            The request body must be a JSON-encoded list of items, where each item contains:
                - id (int): The ID of the product to be ordered.
                - quantity (int): The quantity of the product.

        Returns:
            JsonResponse:
                - On success (HTTP 201): A JSON response with 'status' as 'success' and the 'order_id'.
                - On failure (HTTP 400): A JSON response with 'status' as 'error' and an error message.
                - On incorrect method (HTTP 405): A JSON response indicating that only POST is accepted.

        Raises:
            Product.DoesNotExist: If the product with the provided ID does not exist.
            Exception: For any other exceptions during the order creation process.
        """
        try:
            order_payload = json.loads(request.body.decode('utf-8'))
            order = Order.objects.create(table_id=order_payload["table_id"])

            for item in order_payload["selected_products"]:
                product = Product.objects.get(id=item['id'])
                quantity = item['quantity']
                order_item_repository.create(order, product, quantity)

            return JsonResponse({'status': 'success', 'order_id': order.id}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve orders that are not canceled or finished.
        """
        orders = Order.objects.exclude(status__in=['canceled', 'finished'])

        orders_list = []

        for order in orders:
            order_items = order.items.values(
                'id', 'product__name', "product__category__name", 'quantity'
            )

            orders_list.append({
                'id': order.id,
                'table_id': order.table_id,
                'status': order.status,
                'created_at': order.created_at,
                'items': list(order_items)
            })
        return JsonResponse({'status': 'success', 'orders': orders_list}, status=200)


@require_http_methods(["POST", "PUT"])
@csrf_exempt
def downgrade_order_status_view(_request, order_id: int):
    order = order_repository.get(order_id)
    downgraded_status = order_service.get_downgraded_status(order.status)
    if order.status != downgraded_status:
        order_repository.update_status(order_id, downgraded_status)
        return HttpResponse(f"Order status upgraded to {downgraded_status}")
    return HttpResponse(f"Order already in the lowest status")


@require_http_methods(["POST", "PUT"])
@csrf_exempt
def upgrade_order_status_view(_request, order_id: int):
    order = order_repository.get(order_id)
    upgraded_status = order_service.get_upgraded_status(order.status)
    if order.status != upgraded_status:
        order_repository.update_status(order_id, upgraded_status)
        return HttpResponse(f"Order status upgraded to {upgraded_status}")
    return HttpResponse("Order already in the highest status")
