from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions 



class UserList(generics.ListCreateAPIView):
    
    """ Представление для создания пользователя """
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для получения, обновления и удаления пользователя """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
