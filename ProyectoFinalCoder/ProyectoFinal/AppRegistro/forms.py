from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    image_avatar = forms.ImageField(required=False)

    class Meta:

        model = User
        fields = ['username','email','password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}
        

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


