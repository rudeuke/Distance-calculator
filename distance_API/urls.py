from django.urls import path
from .views import calculate_distance

app_name = 'distance-api'

urlpatterns = [
    path('calculate-distance/', calculate_distance, name='calculate-distance'),
]