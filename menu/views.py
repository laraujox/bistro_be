import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from menu.models import Product, Order, OrderItem, Category
from menu.repositories import OrderItemRepository
from menu.serializers import ProductSerializer, CategorySerializer

order_item_repository = OrderItemRepository()


class ListProducts(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class ListCategories(generics.ListAPIView):
    queryset = Category.objects.filter(available=True)
    serializer_class = CategorySerializer


@csrf_exempt
def create_order(request: WSGIRequest):
    if request.method == 'POST':
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
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST method is accepted'}, status=405)