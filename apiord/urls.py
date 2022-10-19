from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/cars', views.CarModelCreate.as_view({'get': 'list', 'post': 'create'})),
    path('api/cars/<int:pk>', views.CarModelCreate.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/colour', views.ColourApiSerializer.as_view({'get': 'list', 'post': 'create'})),
    path('api/colour/<int:pk>', views.ColourApiSerializer.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/orders', views.OrderCreateList.as_view({'get': 'list', 'post': 'create'})),
    path('api/orders/<int:pk>', views.OrderCreateList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
