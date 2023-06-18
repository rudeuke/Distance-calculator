from django.contrib import admin
from django.urls import path
from distance_calculator.views import calculator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculator),
]