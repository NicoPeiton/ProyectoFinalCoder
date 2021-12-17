from django import forms

class UsuarioForm(forms.Form):

    nombreUsuario = forms.CharField(max_length=10)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=10)
    esAdmin = forms.BooleanField()
    fechaNacimiento = forms.DateField()

class SuscriptorForm(forms.Form):

    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=15)
    profesion = forms.CharField(max_length=30)
    fechaNacimiento = forms.DateField()
    email = forms.EmailField()
