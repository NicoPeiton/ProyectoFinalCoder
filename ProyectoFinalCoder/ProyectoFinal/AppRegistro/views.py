from django.shortcuts import render

from .models import Usuario
from .forms import UsuarioForm


def inicio(request):
    return render(request, "AppRegistro/index.html")

def registro(request):

    if request.method == 'POST':

        miFormulario = UsuarioForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            registroInsta = Usuario(
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

    return render(request, "AppRegistro/registro.html", {"miFormulario":miFormulario}) 