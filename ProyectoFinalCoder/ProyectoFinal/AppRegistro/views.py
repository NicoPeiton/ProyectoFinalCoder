from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Redactor, Suscriptor, Usuario
from .forms import *
from django.contrib.auth.decorators import login_required


def registro(request):
    return render(request, "AppRegistro/registro.html")

def inicio(request):
    return render(request, "AppRegistro/index.html")

def quienes(request):

    return render(request, "AppRegistro/quienes.html")


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppRegistro/index.html", {"mensaje":f"Usuario {username} creado con éxito"})

    else:

        form = UserRegisterForm()

    return render(request, "AppRegistro/register.html", {"form":form})



@login_required(login_url="/AppLogin/login")
def registroUsuario(request):

    if request.method == 'POST':

        miFormulario = UsuarioForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            registroInsta = Usuario(

                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                nombreUsuario=informacion['nombreUsuario'], 
                email=informacion['email'], 
                contraseña=informacion['contraseña'], 
                esAdmin=informacion['esAdmin'], 
                fechaNacimiento=informacion['fechaNacimiento']
            )

            registroInsta.save()

            return render(request, "AppRegistro/index.html")

    else:
        miFormulario = UsuarioForm()

    return render(request, "AppRegistro/registroUsuario.html", {"miFormulario":miFormulario}) 


@login_required(login_url="/AppLogin/login")
def registroRedactor(request):

    if request.method == 'POST':

        miFormulario = RedactorForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            registroInsta = Redactor(

                nombre = informacion['nombre'],
                apellido = informacion['apellido'], 
                email=informacion['email'], 
                contraseña=informacion['contraseña'], 
                profesion=informacion['profesion'], 
                fechaNacimiento=informacion['fechaNacimiento']
            )

            registroInsta.save()

            return render(request, "AppRegistro/index.html")

    else:
        miFormulario = RedactorForm()

    return render(request, "AppRegistro/registroRedactor.html", {"miFormulario":miFormulario}) 


@login_required(login_url="/AppLogin/login")
def registroSuscriptor(request):

    if request.method == 'POST':

        miFormulario = SuscriptorForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            registroInsta = Suscriptor(

                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                email=informacion['email'], 
                profesion=informacion['profesion'], 
                fechaNacimiento=informacion['fechaNacimiento']
            )

            registroInsta.save()

            return render(request, "AppRegistro/index.html")

    else:
        miFormulario = SuscriptorForm()

    return render(request, "AppRegistro/registroSuscriptor.html", {"miFormulario":miFormulario}) 