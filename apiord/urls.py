from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/cars', views.CarModelCreate.as_view({'get': 'list', 'post': 'create'})),
    # path('api/models/create',),,
    # path('api/orders/get/<int:pk>',),
    path('api/orders', views.OrderCreateList.as_view({'get': 'list', 'post': 'create'})),
    path('api/orders/v2', views.orders),
]
