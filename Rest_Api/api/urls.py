from django.urls import path
from . import views

urlpatterns = [
    path('calcClosestPath/', views.employeeList.as_view()),
    path('getClosestPath/', views.employeeList.as_view()),
]