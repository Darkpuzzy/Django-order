from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=150, verbose_name='Brand')

    def __str__(self):
        return self.name


class Colour(models.Model):
    colour = models.CharField(max_length=150, verbose_name='Colour')

    def __str__(self):
        return self.colour


class CarsModel(models.Model):
    model = models.CharField(max_length=150, verbose_name='Model')

    def __str__(self):
        return self.model


class Order(models.Model):
    order_ticket = models.CharField(max_length=150, verbose_name='Order number')
    car = models.ManyToManyField(Car, verbose_name='Brand')
    model = models.ManyToManyField(CarsModel, verbose_name='Model')
    colour = models.ManyToManyField(Colour, verbose_name='Colour')
    quantity = models.IntegerField(default=0, verbose_name='Quantity of cars')
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='Date of order')

    def __str__(self):
        return self.order_ticket
