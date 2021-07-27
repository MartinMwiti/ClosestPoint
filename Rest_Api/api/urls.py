from django.urls import path
from . import views

urlpatterns = [
    path('calcClosestPath/', views.closestDistanceValue.as_view()),
    path('getClosestPath/', views.closestDistanceValue.as_view()),
]