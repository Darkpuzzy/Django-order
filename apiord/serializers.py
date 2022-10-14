from rest_framework import serializers
from apiord.models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('car', 'model', 'colour', 'quantity', 'date_order')
