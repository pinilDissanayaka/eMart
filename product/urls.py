from django.urls import path, include
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("men/", view=views.men_product_view, name="men"),
    path("women/", view=views.women_product_view, name="women"),
    path("kids/", view=views.kids_product_view, name="kids"),
]