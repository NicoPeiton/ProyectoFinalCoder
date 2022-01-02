from django.db import models

class Usuario(models.Model):

    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    nombreUsuario = models.CharField(max_length=10)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)
    esAdmin = models.BooleanField()
    fechaNacimiento = models.DateField()  

    def __str__(self):
        return f"Usuario: {self.nombreUsuario} Email: {self.email}"

class Redactor(models.Model):

    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)
    profesion = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()

    def __str__(self):
        return f"Usuario: {self.nombre} Email: {self.email}"

class Suscriptor(models.Model):

    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()

    def __str__(self):
        return f"Usuario: {self.nombre} Email: {self.email}"
