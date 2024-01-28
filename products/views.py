from django.shortcuts import render
from .models import Product, ProductCategory, ProductImage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ProcsAdmin.decorators import IsProcsAdmin
from .serializers import ProductCategorySerializer, ProductSerializer
from orders.serializers import OrderSerializer
from orders.models import Order, OrderItem

    
@api_view(['PUT', 'PATCH', 'DELETE', 'GET', 'POST'])
@permission_classes([IsAuthenticated])
def singleProduct(request, pid):
    product = Product.objects.get(id=pid)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    
    if request.method == 'POST':
        order, created = Order.objects.get_or_create(
            buyer=request.user,
            status="Pending"
        )

        data = request.data

        OrderItem.objects.create(
            product = product,
            order = order,
            quantity = data['quantity'],
        )

        serializer = OrderSerializer(order, many=False)

        return Response(serializer.data)

    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def Products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)