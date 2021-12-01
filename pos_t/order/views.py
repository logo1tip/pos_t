from order.models import Table, Dish, Order
from order.serializers import TableSerializer, DishSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from order.permissions import IsAdministrator, IsCook, IsWaiter


class TableList(generics.ListCreateAPIView):

    """ Представление для получения списка столиков """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdministrator]


class TableDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для получения, обновления и удаления столиков """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdministrator]


class DishList(generics.ListCreateAPIView):

    """ Представление для получения списка блюд """

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdministrator]


class DishDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для получения, обновления и удаления блюд """

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdministrator]


class OrderList(generics.ListCreateAPIView):

    """ Представление для получения списка заказов """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdministrator|IsWaiter|IsCook]


class OrderRU(generics.RetrieveUpdateAPIView):

    """ Представление для получения и обновления блюд """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdministrator|IsWaiter]


class OrderDestroy(generics.DestroyAPIView):

    """ Представление для удаления блюд """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdministrator|IsCook]

