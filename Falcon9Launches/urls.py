from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('boosters', views.boosters, name="boosters"),
    path('boosters/<int:booster_id>', views.boosterDetails, name="boosterDetails"),
    path('boosters/<int:booster_id>/edit', views.boosterEdit, name="boosterEdit"),
    path('boosters/<int:booster_id>/delete', views.boosterDelete, name="boosterDelete"),
    path('launchcomplexes', views.launchcomplexes, name="launchcomplexes"),
    path('launchcomplexes/<int:complex_id>', views.complexDetails, name="complexDetails"),
    path('launchsites', views.launchsites, name="launchsites"),
    path('launchsites/<int:site_id>', views.launchSiteDetails, name="launchSiteDetails"),
    path('missions', views.missions, name="missions"),
    path('flights', views.flights, name="flights"),
    path('flights/<int:flight_id>', views.flightDetails, name="flightDetails"),
    path('photos', views.photos, name='photos')
]   
