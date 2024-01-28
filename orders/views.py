from django.shortcuts import render
from .models import Shipping_Address, Order, OrderItem
from users.models import ProcsUser
from rest_framework.response import Response
from .serializers import AddressSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAddress(request):
    if request.method == 'POST':
        data = request.data
        user = request.user
        print(user)
        address = Shipping_Address.objects.create(
            address = data['address'],
            user = request.user,
            postal_code = data['postal_code'],
            person = data['person'],
            contact = data['contact'],
        )
    
    serializer = AddressSerializer(address, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAddress(request, aid):
    if request.method == 'PUT':
        data = request.data
        user = request.user
        addresss = Shipping_Address.objects.get(id=aid)

        if 'address' in data:
            addresss.address = data['address']
        addresss.save()
        serializer = AddressSerializer(addresss, many=False)
        return Response(serializer.data)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delAddress(request, aid):
    if request.method == 'DELETE':
        address = Shipping_Address.objects.get(id=aid)
        address.delete()

        return Response('Address Deleted')

