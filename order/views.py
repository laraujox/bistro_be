import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from menu.models import Product
from order.models import Order
from order.repositories import OrderItemRepository

order_item_repository = OrderItemRepository()


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
            items = json.loads(request.body.decode('utf-8'))
            order = Order.objects.create()

            for item in items:
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

        # Convert the QuerySet to a list of dictionaries
        orders_list = list(orders.values())

        return JsonResponse({'status': 'success', 'orders': orders_list}, status=200)
