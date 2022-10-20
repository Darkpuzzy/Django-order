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

    def validate(self, attrs):
        model = attrs.get('model')
        car_id = Car.objects.get(name=attrs.get('car').get('name'))
        bool = CarsModel.objects.filter(model=model, car_id=car_id.id).exists()
        if bool:
            raise serializers.ValidationError(
                {"This model already exists"})
        return attrs

    def create(self, validated_data):
        obj, created = Car.objects.get_or_create(name=validated_data.get('car').get('name'))
        cmod = CarsModel.objects.create(model=validated_data.get('model', ''),
                                        car_id=obj.id)
        return cmod

    def update(self, instance, validated_data):
        car_id = Car.objects.get(name=validated_data.get('car').get('name'))
        instance.model = validated_data.get('model', instance.model)
        instance.car_id = car_id.id
        instance.save()

        return instance


class ColourSerializers(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = ('colour',)

    def validate(self, attrs):
        colour = attrs.get('colour')
        bool = Colour.objects.filter(colour=colour).exists()
        if bool:
            raise serializers.ValidationError(
                {"This colour already exists"})
        return attrs


class OrderSerializersGet(serializers.ModelSerializer):
    model = CarsModelSerializers()
    colour = ColourSerializers()

    class Meta:
        model = Order
        fields = ('model', 'colour', 'quantity', 'date_order')
        read_only_fields = ('id', 'date_order')


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('model', 'colour', 'quantity', 'date_order')
        read_only_fields = ('id', 'date_order')


class ColourQuantitySerializers(serializers.ModelSerializer):
    colour = ColourSerializers()

    class Meta:
        model = Order
        fields = ('colour', 'quantity')

# #TODO on method GET/POST v2
# class OrdersSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Order
#         fields = ('model', 'colour', 'quantity', 'date_order')
#         read_only_fields = ('id', 'date_order')
#
#     def create(self, validated_data):
#         order = Order.objects.create(
#                                    model_id=validated_data.get('model', 0),
#                                    colour_id=validated_data.get('colour', 0),
#                                    quantity=validated_data.get('quantity', 0))
#
#         return order
#
#     def update(self, instance, validated_data):
#         instance.model_id = validated_data.get('model', instance.model)
#         instance.colour_id = validated_data.get('colour', instance.colour)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.save()
#
#         return instance