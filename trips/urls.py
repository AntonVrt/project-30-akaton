from django.urls import path
from django.urls.resolvers import URLResolver
from . import views


urlpatterns = [ 
     path('', views.trips,name="trips"),
     path('trip/<str:pk>/',views.trip,name="trip"),
]