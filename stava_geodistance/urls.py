from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('distance_calculator.urls')),
    path('api/', include('distance_API.urls', namespace='distance-api')),
]