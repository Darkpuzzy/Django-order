from datetime import datetime
from rest_framework import serializers
from apiord.models import *


class CarSerializers(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('name',)


class CarsModelSerializers(serializers.ModelSerializer):
    car = CarSerializers()

    class Meta:
        model = CarsModel
        fields = ('model', 'car')


class ColourSerializers(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = ('colour',)


#TODO на POST
class OrderSerializers(serializers.ModelSerializer):
    # model = CarsModelSerializers()
    # colour = ColourSerializers()

    class Meta:
        model = Order
        fields = ('model', 'colour', 'quantity', 'date_order')
        read_only_fields = ('id', 'date_order')


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('model', 'colour', 'quantity', 'date_order')
        read_only_fields = ('id', 'date_order')

    def create(self, validated_data):
        order = Order.objects.create(
                                   model_id=validated_data.get('model', 0),
                                   colour_id=validated_data.get('colour', 0),
                                   quantity=validated_data.get('quantity', 0))

        return order

    def update(self, instance, validated_data):
        instance.model_id = validated_data.get('model', instance.model)
        instance.colour_id = validated_data.get('colour', instance.colour)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()

        return instance