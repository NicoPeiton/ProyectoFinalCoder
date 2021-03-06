from django.urls import path
from AppPerfiles import views
from AppPerfiles.views import PerfilUsuario, PerfilRedactor, PerfilSuscriptor

urlpatterns = [
    path('buscarPerfiles', views.buscarPerfiles, name='Buscar usuario'),
    path('buscar/', views.buscar),
    path('verPerfiles', views.verPerfiles, name='Ver Perfiles'),
    path(r'^usuario/(?P<pk>\d+)$', views.PerfilUsuario.as_view(), name='Perfil Usuario'),
    path(r'^redactor/(?P<pk>\d+)$', views.PerfilRedactor.as_view(), name='Perfil Redactor'),
    path(r'^suscriptor/(?P<pk>\d+)$', views.PerfilSuscriptor.as_view(), name='Perfil Suscriptor'),
    path('editarAdmin', views.editarAdmin, name='Editar Admin'),
    path('eliminarUsuario/<id_usuario>', views.eliminarUsuario, name='Eliminar Usuario'),
    path('eliminarRedactor/<id_redactor>', views.eliminarRedactor, name='Eliminar Redactor'),
    path('eliminarSuscriptor/<id_suscriptor>', views.eliminarSuscriptor, name='Eliminar Suscriptor'),
    path('editarUsuario/<id_usuario>', views.editarUsuario, name='Editar Usuario'),
    path('editarRedactor/<id_redactor>', views.editarRedactor, name='Editar Redactor'),
    path('editarSuscriptor/<id_suscriptor>', views.editarSuscriptor, name='Editar Suscriptor'),
]