from django.urls import path
from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


schema_view = get_schema_view(
   openapi.Info(
      title="Rest API`s",
      default_version='v1',
      description="This api`s for django",
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

doc_url = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

cars_url = [
    path('cars', views.CarModelCreate.as_view({'get': 'list', 'post': 'create'})),
    path('cars/<int:pk>', views.CarModelCreate.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

colour_url = [
    path('colour', views.ColourApiSerializer.as_view({'get': 'list', 'post': 'create'})),
    path('colour/<int:pk>', views.ColourApiSerializer.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

orders_url = [
    path('orders', views.OrderCreateList.as_view({'get': 'list', 'post': 'create'})),
    path('orders/<int:pk>', views.OrderCreateList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

cq_url = [
    path('order/colour', views.ColorQuantity.as_view({'get': 'list'}))
]

urlpatterns = [
    path('', include(orders_url)),
    path('', include(colour_url)),
    path('', include(cars_url)),
    path('', include(cq_url)),
    path('v2/', views.index)
]
