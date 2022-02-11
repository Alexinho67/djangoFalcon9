from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('boosters', views.boosters, name="boosters"),
    path('boosters/create', views.boosterCreate, name="boosterCreate"),
]   