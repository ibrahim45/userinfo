from django.shortcuts import render
from details.models import Customer
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from details.serializers import CustomerSerializer


@api_view(['GET', 'POST'])
def view_all(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'GET'])
def update_or_delete(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

