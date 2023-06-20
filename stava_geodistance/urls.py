from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('distance_calculator.urls')),
    path('API/', include('distance_API.urls')),
]