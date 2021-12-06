from order.models import Table, Dish, Order
from order.serializers import TableSerializer, DishSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from order.permissions import IsAdministrator, IsCook, IsWaiter
from drf_spectacular.utils import extend_schema


@extend_schema(description='Admin only')
class TableList(generics.ListCreateAPIView):

    """ Представление для получения списка столиков """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdminUser|IsAdministrator]


@extend_schema(description='Admin only')
class TableDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для получения, обновления и удаления столиков """

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAdminUser|IsAdministrator]


@extend_schema(description='Admin only')
class DishList(generics.ListCreateAPIView):

    """ Представление для получения списка блюд """

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUser|IsAdministrator]


@extend_schema(description='Admin only')
class DishDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для получения, обновления и удаления блюд """

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUser|IsAdministrator|IsWaiter]


@extend_schema(description='Admin only')
class OrderList(generics.ListCreateAPIView):

    """ Представление для получения списка заказов """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser|IsAdministrator|IsWaiter|IsCook]


@extend_schema(description='Admin only')
class OrderRU(generics.RetrieveUpdateAPIView):

    """ Представление для получения и обновления блюд """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser|IsAdministrator|IsWaiter]


@extend_schema(description='Admin only')
class OrderDestroy(generics.DestroyAPIView):

    """ Представление для удаления блюд """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser|IsAdministrator|IsCook]

