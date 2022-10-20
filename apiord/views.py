from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from .serializers import OrderSerializers, CarSerializers, CarsModelSerializers,\
    ColourSerializers, OrderSerializersGet, ColourQuantitySerializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class OrderCreateList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializersGet
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quantity', 'model__car']

    def get_serializer_class(self):
        methods = ['POST', 'PUT']
        if self.request.method in methods:
            return OrderSerializers
        return self.serializer_class


class CarModelCreate(viewsets.ModelViewSet):
    queryset = CarsModel.objects.all()
    serializer_class = CarsModelSerializers
    pagination_class = StandardResultsSetPagination


class ColourApiSerializer(viewsets.ModelViewSet):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializers
    pagination_class = StandardResultsSetPagination


class ColorQuantity(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = ColourQuantitySerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quantity']


@api_view(['GET'])
def index(request):
    list_response = []
    status_code = status.HTTP_200_OK
    colour_id = Colour.objects.all()
    for c_i in colour_id:
        response = {}
        model = Order.objects.filter(colour_id=c_i.id)
        count = 0
        for i in model:
            if i.quantity > 0:
                count += i.quantity
                response['colour'] = c_i.id
                response['quantity'] = count
            print(response)
        list_response.append(response)

    return Response(list_response, status=status_code)




    # response = {
    #     'colour': model.order,
    #     'quantity': model.price_dlr
    # }
    # print(_updated_data(list_data=list_to_db))
    # print(added_to_db(list_data=list_to_db))
    # return Response(response, status=status_code)
