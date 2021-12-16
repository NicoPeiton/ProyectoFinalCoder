from django.db import models

class Login(models.Model):

    nombreUsuario = models.CharField(max_length=10)
    contraseña = models.CharField(max_length=10) 
