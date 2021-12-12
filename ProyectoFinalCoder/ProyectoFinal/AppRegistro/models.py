from django.db import models

class Usuario(models.Model):

    nombreUsuario = models.CharField(max_length=10)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)