from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser 
from order.permissions import IsAdministrator



class UserList(generics.ListCreateAPIView):
    
    """ Представление для получения списка пользователей """
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser|IsAdministrator]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для получения, обновления и удаления пользователя """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser|IsAdministrator]
