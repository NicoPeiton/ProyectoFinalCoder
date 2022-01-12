from django.contrib.auth.views import redirect_to_login
from django.http.response import HttpResponse
from django.shortcuts import render
from AppRegistro.models import *
from AppRegistro.forms import * 
from django.contrib.auth.decorators import login_required
from AppPerfiles.forms import UserEditForm
from django.views.generic.detail import DetailView


def buscarPerfiles(request):

    return render(request, "AppPerfiles/buscarPerfiles.html")


def verPerfiles(request):

    usuarios = Usuario.objects.all()

    redactores = Redactor.objects.all()

    suscriptores = Suscriptor.objects.all()

    contexto = {"usuarios":usuarios, "redactores": redactores, "suscriptores": suscriptores}

    return render(request, "AppPerfiles/verPerfiles.html", contexto)
    

class PerfilUsuario(DetailView):

    model = Usuario
    template_name = "AppPerfiles/perfilUsuario.html"

class PerfilRedactor(DetailView):

    model = Redactor
    template_name = "AppPerfiles/perfilRedactor.html"

class PerfilSuscriptor(DetailView):

    model = Suscriptor
    template_name = "AppPerfiles/perfilSuscriptor.html"


def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        
        redactores = Redactor.objects.filter(nombre__icontains=nombre)

        suscriptores = Suscriptor.objects.filter(nombre__icontains=nombre)

        return render(request, "AppPerfiles/resultadoBusqueda.html", {"usuarios":usuarios, "redactores":redactores, "suscriptores":suscriptores, "nombre":nombre})

    else: 
        return render(request, "AppPerfiles/buscarPerfiles.html")


@login_required(login_url="/AppLogin/login")
def editarAdmin(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "AppRegistro/index.html")

    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "AppPerfiles/editarAdmin.html", {"miFormulario":miFormulario, "usuario": usuario})


@login_required(login_url="/AppLogin/login")
def eliminarUsuario(request, id_usuario):

    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()

    usuarios = Usuario.objects.all()

    redactores = Redactor.objects.all()

    suscriptores = Suscriptor.objects.all()

    contexto = {"usuarios":usuarios, "redactores":redactores, "suscriptores":suscriptores}

    return render(request, "AppPerfiles/verPerfiles.html", contexto)


@login_required(login_url="/AppLogin/login")
def eliminarRedactor(request, id_redactor):

    redactor = Redactor.objects.get(id=id_redactor)
    redactor.delete()

    usuarios = Usuario.objects.all()

    redactores = Redactor.objects.all()

    suscriptores = Suscriptor.objects.all()

    contexto = {"usuarios":usuarios, "redactores":redactores, "suscriptores":suscriptores}

    return render(request, "AppPerfiles/verPerfiles.html", contexto)


@login_required(login_url="/AppLogin/login")
def eliminarSuscriptor(request, id_suscriptor):

    suscriptor = Suscriptor.objects.get(id=id_suscriptor)
    suscriptor.delete()

    usuarios = Usuario.objects.all()

    redactores = Redactor.objects.all()

    suscriptores = Suscriptor.objects.all()

    contexto = {"usuarios":usuarios, "redactores":redactores, "suscriptores":suscriptores}

    return render(request, "AppPerfiles/verPerfiles.html", contexto)


@login_required(login_url="/AppLogin/login")
def editarUsuario(request, id_usuario):

    usuario = Usuario.objects.get(id=id_usuario)

    if request.method == 'POST':

        miFormulario = UsuarioForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre'],
            usuario.apellido = informacion['apellido']
            usuario.nombreUsuario = informacion['nombreUsuario']
            usuario.email = informacion['email']
            usuario.contraseña = informacion['contraseña']
            usuario.esAdmin = informacion['esAdmin']
            usuario.fechaNacimiento = informacion['fechaNacimiento']

            usuario.save()

            return render(request, "AppPerfiles/verPerfiles.html")

    else:
        miFormulario = UsuarioForm(initial={'nombre':usuario.nombre, 'apellido':usuario.apellido,
         'nombreUsuario':usuario.nombreUsuario, 'email':usuario.email, 'contraseña':usuario.contraseña, 
         'esAdmin':usuario.esAdmin, 'fechaNacimiento':usuario.fechaNacimiento})

    return render(request, "AppPerfiles/editarUsuario.html", {"miFormulario":miFormulario, "id_usuario":id_usuario}) 


@login_required(login_url="/AppLogin/login")
def editarRedactor(request, id_redactor):

    redactor = Redactor.objects.get(id=id_redactor)

    if request.method == 'POST':

        miFormulario = RedactorForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            redactor.nombre = informacion['nombre']
            redactor.apellido = informacion['apellido']
            redactor.email = informacion['email']
            redactor.contraseña = informacion['contraseña']
            redactor.profesion = informacion['profesion']
            redactor.fechaNacimiento = informacion['fechaNacimiento']

            redactor.save()

            return render(request, "AppPerfiles/verPerfiles.html")

    else:
        miFormulario = RedactorForm(initial={'nombre':redactor.nombre, 'apellido':redactor.apellido, 
        'email':redactor.email, 'contraseña':redactor.contraseña, 'profesion':redactor.profesion, 'fechaNacimiento':redactor.fechaNacimiento})

    return render(request, "AppPerfiles/editarRedactor.html", {"miFormulario":miFormulario, "id_redactor":id_redactor}) 


@login_required(login_url="/AppLogin/login")
def editarSuscriptor(request, id_suscriptor):

    suscriptor = Suscriptor.objects.get(id=id_suscriptor)

    if request.method == 'POST':

        miFormulario = SuscriptorForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            suscriptor.nombre = informacion['nombre']
            suscriptor.apellido = informacion['apellido']
            suscriptor.email = informacion['email']
            suscriptor.profesion = informacion['profesion'] 
            suscriptor.fechaNacimiento = informacion['fechaNacimiento']
            
            suscriptor.save()

            return render(request, "AppPerfiles/verPerfiles.html")

    else:
        miFormulario = SuscriptorForm(initial={'nombre':suscriptor.nombre, 'apellido':suscriptor.apellido,
        'email':suscriptor.email, 'profesion':suscriptor.profesion, 'fechaNacimiento':suscriptor.fechaNacimiento})

    return render(request, "AppPerfiles/editarSuscriptor.html", {"miFormulario":miFormulario, "id_suscriptor":id_suscriptor})