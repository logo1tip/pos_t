from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser


class AdminUser(UserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "role",
        "is_staff",
    )
    list_display_links = ("id", "first_name", "last_name")
    list_filter = ("is_staff",)
    search_fields = ("first_name", "role")
    ordering = ("last_name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "phone",
                    "password",
                    "groups",
                    "role",
                    "is_staff",
                )
            },
        ),
    )



admin.site.register(CustomUser, AdminUser)


