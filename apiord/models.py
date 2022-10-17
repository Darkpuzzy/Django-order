from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=150, verbose_name='Brand')

    def __str__(self):
        return self.name


class CarsModel(models.Model):
    model = models.CharField(max_length=150, verbose_name='Model', null=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)

    def __str__(self):
        return self.model


class Colour(models.Model):
    colour = models.CharField(max_length=150, verbose_name='Colour')

    def __str__(self):
        return self.colour


class Order(models.Model):
    # order_ticket = models.CharField(max_length=150, verbose_name='Order number')
    # car = models.ForeignKey(Car, verbose_name='Model', on_delete=models.PROTECT)
    model = models.ForeignKey(CarsModel, verbose_name='Model', on_delete=models.PROTECT)
    colour = models.ForeignKey(Colour, verbose_name='Colour', on_delete=models.PROTECT, null=True)
    quantity = models.IntegerField(default=0, verbose_name='Quantity of cars')
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='Date of order')

    # def __str__(self):
    #     return self.order_ticket
