from rest_framework.serializers import ModelSerializer
from user.models import CustomUser


class UserSerializer(ModelSerializer):

    """ Сериализатор для модели пользователя """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name",
         "password", "phone", "role"
         )