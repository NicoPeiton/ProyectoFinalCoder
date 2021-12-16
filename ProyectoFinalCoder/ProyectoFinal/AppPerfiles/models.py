from django.db import models

class Admin(models.Model):

    nombreUsuario = models.CharField(max_length=10)
    esAdmin = models.BooleanField(True)

class User(models.Model):

    nombreUsuario = models.CharField(max_length=10)
    esAdmin = models.BooleanField(False)
