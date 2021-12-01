from django.db import models


class Table(models.Model):

    """ Модель столика """

    number = models.PositiveIntegerField(unique=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return f'Table № {self.number}'


class Dish(models.Model):

    """ Модель блюда """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.name


class Order(models.Model):

    """ Модель заказа """

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    dishs = models.ForeignKey(Dish, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField("Dish amount", default=1)


