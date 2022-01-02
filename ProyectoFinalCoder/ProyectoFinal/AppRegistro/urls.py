from django.urls import path
from AppRegistro import views

urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path("quienes", views.quienes, name='Quiénes'),
    path('registro', views.registro, name='Registrarse'),
    path('registroUsuario', views.registroUsuario, name='Usuario'),
    path('registroRedactor', views.registroRedactor, name='Redactor'),
    path('registroSuscriptor', views.registroSuscriptor, name='Suscriptor'),
]