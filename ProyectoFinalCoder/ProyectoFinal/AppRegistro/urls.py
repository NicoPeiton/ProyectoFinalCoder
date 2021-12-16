from django.urls import path
from AppRegistro import views

urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path('registro', views.registro, name='Registrarse'),
]