from django.contrib import admin
from order.models import Table, Dish, Order


class DishAdmin(admin.ModelAdmin):

    """ Административная панель блюда """

    list_display = ["id", "name", "price"]
    list_display_links = ("id", "name")
    ordering = ("name",)


class OrderAdmin(admin.ModelAdmin):

    """ Административная панель заказа """

    list_display = ["id", "table", "dishs"]
    list_display_links = ("id", "table")
    ordering = ("table",)



admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Table)

