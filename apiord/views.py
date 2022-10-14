from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import OrderSerializers


class OrderCreateList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers