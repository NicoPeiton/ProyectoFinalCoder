from django.urls import path
from AppPerfiles import views

urlpatterns = [
    path('perfiles', views.perfiles, name='Buscar usuario'),
]