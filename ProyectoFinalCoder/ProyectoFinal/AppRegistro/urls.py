from django.urls import path
from AppRegistro import views

urlpatterns = [
    path('registro', views.registro),
]