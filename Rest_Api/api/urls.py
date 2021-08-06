from django.urls import path
from . import views

urlpatterns = [
    path('calcClosestPath/', views.closestDistanceValue.as_view(), name='calcClosestDistance'),
    path('getClosestPath/', views.closestDistanceValue.as_view(), name='getClosestDistance'),
]