from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order.views import *



urlpatterns = [
    path("tables/", TableList.as_view()),
    path("tables/<int:pk>/", TableDetail.as_view()),
    path("dishs/", DishList.as_view()),
    path("dishs/<int:pk>/", DishDetail.as_view()),
    path("orders/", OrderList.as_view()),
    path("orders/<int:pk>/", OrderRU.as_view()),
    path("orders/destroy/<int:pk>/", OrderDestroy.as_view()),   
]

urlpatterns = format_suffix_patterns(urlpatterns)