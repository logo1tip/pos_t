from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from user.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]
