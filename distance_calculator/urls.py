from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculatorInput),
    path('<str:temp1>/<str:pointsString>/', views.processData),
]
