from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('stava-geodistance/', include('distance_calculator.urls')),
    path('stava-geodistance/', include('distance_API.urls')),
]