from django.urls import path
from .views import calculate_distance

urlpatterns = [
    path('calculate-distance/', calculate_distance, name='calculate-distance'),
]