from django.urls import include, path
from . import views

urlpatterns = [
    path('stava-geodistance/', include('stava_geodistance.urls')),
]
