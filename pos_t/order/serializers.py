from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from order.models import Table, Dish, Order


class TableSerializer(ModelSerializer):

    """ Сериализатор для модели столика """

    class Meta:
        model = Table
        fields = ("id", "number", "is_active")


class DishSerializer(ModelSerializer):

    """ Сериализатор для модели блюда """

    class Meta:
        model = Dish
        fields = ("id", "name", "description", "price")


class OrderSerializer(ModelSerializer):

    """ Сериализатор для модели заказа """

    class Meta:
        model = Order
        fields = ("id", "table", "dishs", "quantity")