from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('boosters', views.boosters, name="boosters"),
    path('launchcomplexes', views.launchcomplexes, name="launchcomplexes"),
    path('missions', views.missions, name="missions"),
    path('flights', views.flights, name="flights"),
    path('boosters/delete/<int:id_booster>', views.boosterDelete, name="boostersDelete"),
    path('photos', views.photos, name='photos')
]   