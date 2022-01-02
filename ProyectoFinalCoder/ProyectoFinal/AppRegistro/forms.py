from django import forms

class UsuarioForm(forms.Form):

    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=15)
    nombreUsuario = forms.CharField(max_length=10)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=10)
    esAdmin = forms.NullBooleanField()
    fechaNacimiento = forms.DateField()   

class RedactorForm(forms.Form):

    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=15)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=10)
    profesion = forms.CharField(max_length=30)
    fechaNacimiento = forms.DateField()
    
class SuscriptorForm(forms.Form):

    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=15)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    fechaNacimiento = forms.DateField()
