from django.urls import path
from AppPerfiles import views

urlpatterns = [
    path('buscarPerfiles', views.buscarPerfiles, name='Buscar usuario'),
    path('buscar/', views.buscar),
]