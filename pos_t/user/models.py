import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class _PhoneValidator:

    _pattern = re.compile(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")

    def __call__(self, value):
        if not self._pattern.match(value):
            raise ValidationError("{!r}, Value is not phone number.".format(value))


class CustomUser(AbstractUser):

    ADMINISTRATOR = "AD"
    WAITER = "WT"
    COOK = "CK"
    ROLE = [
        (ADMINISTRATOR, "Administrator"),
        (WAITER, "Waiter"),
        (COOK, "Cook"),
    ]
    
    phone = models.CharField(
        max_length=20,
        validators=[_PhoneValidator()],
        null=True,
    )
    role = models.CharField(
        choices=ROLE, 
        max_length=5,
        verbose_name="Role",
    )
        

    def __str__(self):
        return self.email


    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["first_name"]