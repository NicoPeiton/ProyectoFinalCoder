from django.http.response import HttpResponse
from django.shortcuts import render
from AppRegistro.models import * 

def buscarPerfiles(request):

    return render(request, "AppPerfiles/buscarPerfiles.html")


def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        
        redactores = Redactor.objects.filter(nombre__icontains=nombre)

        suscriptores = Suscriptor.objects.filter(nombre__icontains=nombre)

        return render(request, "AppPerfiles/resultadoBusqueda.html", {"usuarios":usuarios, "redactores":redactores, "suscriptores":suscriptores, "nombre":nombre})

    else:
        
        return render(request, "AppPerfiles/buscarPerfiles.html")
