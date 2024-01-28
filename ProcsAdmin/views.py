from django.shortcuts import render
from products.models import Product, ProductCategory, ProductImage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .decorators import IsProcsAdmin
from products.serializers import ProductCategorySerializer, ProductSerializer
from orders.serializers import OrderSerializer
from orders.models import Order, OrderItem

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@IsProcsAdmin
def addProduct(request):
    if request.method == 'POST':
        data = request.data
        print(request.data)
        user = request.user
        images = request.FILES.getlist('images')

        product = Product.objects.create(
            name = data['name'],
            user = user,
            description = data['description'],
            price = data['price'],
            category = ProductCategory.objects.get(id=1),
            quantity = data['quantity'],
        )

        
        for image_file in images:
            ProductImage.objects.create(
                product=product,
                image=image_file,
                isCover=False
            )
    
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)
    
@api_view(['PUT', 'PATCH', 'DELETE', 'GET', 'POST'])
@permission_classes([IsAuthenticated])
@IsProcsAdmin
def singleProduct(request, pid):
    product = Product.objects.get(id=pid)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = request.data
        user = request.user 

        # if 'name' in data:
        #     product.name = data['name']

        # elif 'description' in data:
        #     product.description = data['description']

        # elif 'price' in data:
        #     product.price = data['price']
        
        # elif 'category' in data:
        #     product.quantity = data['quantity']
        
        keys = ['name', 'description', 'price', 'quantity']

        for key in keys:
            if key in data:
                setattr(product, key, data[key])

        product.save()

    if request.method == 'PATCH':
        images = request.FILES.getlist('images')

        for image_file in images:
            ProductImage.objects.create(
                product=product,
                image=image_file,
                isCover=False
            )
    
    if request.method == 'DELETE':
        data = request.data

        if "id" in data:
            image_id = data['id']
            image = ProductImage.objects.get(id=image_id)
            image.delete()
        else:
            product.delete()
            return Response("Item Deleted")

    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@IsProcsAdmin
def Products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@IsProcsAdmin
def Orders(request):
    orders = Order.objects.all()

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@IsProcsAdmin
def singleOrder(request, oid):
    order = Order.objects.get(id=oid)

    serializer = OrderSerializer(order, many=False)

    return Response(serializer.data)
    



