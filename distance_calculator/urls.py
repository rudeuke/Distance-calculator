from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculatorInput),
    path('<str:request_id>/<str:pointsString>/', views.processData),
]
