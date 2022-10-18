from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import *


class OrderCreateList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class CarModelCreate(viewsets.ModelViewSet):
    queryset = CarsModel.objects.all()
    serializer_class = CarsModelSerializers


@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            order = serializer.create(validated_data=request.data)
            response = {
                'model': order.model_id,
                'colour': order.colour_id,
                'quantity': order.quantity,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        order_list = Order.objects.all()
        response_list = []
        for order in order_list:
            response = {
                'model': order.model_id,
                'colour': order.colour_id,
                'quantity': order.quantity,
                'date_order': order.date_order
            }
            response_list.append(response)
        return Response(response_list, status=status.HTTP_200_OK)

# {
#     "model": 1,
#     "colour": 2,
#     "quantity": 3,
#     "date_order": "2022-10-17T13:15:20.252602Z"
#  }