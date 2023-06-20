from django.urls import path
from distance_calculator import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculator),
]
