from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculatorInput),
    path('<str:requestId>/<str:pointsString>/', views.processData),
]
