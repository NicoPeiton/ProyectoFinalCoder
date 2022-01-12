from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:

                login(request, user)

                return render(request, "AppRegistro/index.html", {"mensaje":f"{usuario}"})

            else:

                return render(request, "AppRegistro/index.html", {"mensaje":f"Usuario o contraseña incorrectos"})

        else:

             return render(request, "AppRegistro/index.html", {"mensaje":f"Error al iniciar sesión"})


    form = AuthenticationForm()

    return render(request, 'AppLogin/login.html', {'form':form})
