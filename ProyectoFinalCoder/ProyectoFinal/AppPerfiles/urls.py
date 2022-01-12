from django.urls import path
from AppPerfiles import views

urlpatterns = [
    path('buscarPerfiles', views.buscarPerfiles, name='Buscar usuario'),
    path('buscar/', views.buscar),
    path('verPerfiles', views.verPerfiles, name='Ver Perfiles'),
    path('editarAdmin', views.editarAdmin, name='Editar Admin'),
    path('eliminarUsuario/<id_usuario>', views.eliminarUsuario, name='Eliminar Usuario'),
    path('eliminarRedactor/<id_redactor>', views.eliminarRedactor, name='Eliminar Redactor'),
    path('eliminarSuscriptor/<id_suscriptor>', views.eliminarSuscriptor, name='Eliminar Suscriptor'),
    path('editarUsuario/<id_usuario>', views.editarUsuario, name='Editar Usuario'),
    path('editarRedactor/<id_redactor>', views.editarRedactor, name='Editar Redactor'),
    path('editarSuscriptor/<id_suscriptor>', views.editarSuscriptor, name='Editar Suscriptor'),
]