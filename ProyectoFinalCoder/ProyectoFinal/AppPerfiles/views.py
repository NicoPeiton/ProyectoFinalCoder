from django.shortcuts import render

def perfiles(request):
    return render(request, "AppPerfiles/perfiles.html")
