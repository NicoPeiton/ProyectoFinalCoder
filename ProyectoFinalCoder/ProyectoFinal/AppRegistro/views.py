from django.shortcuts import render

def inicio(request):
    return render(request, "AppRegistro/index.html")

def registro(request):
    return render(request, "AppRegistro/registro.html")