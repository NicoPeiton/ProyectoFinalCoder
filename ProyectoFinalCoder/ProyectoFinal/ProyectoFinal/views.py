from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def inicio(request):

    template = loader.get_template('index.html')

    documento = template.render()

    return HttpResponse(documento)