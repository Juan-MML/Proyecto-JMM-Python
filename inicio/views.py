from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def inicio (request):
    return HttpResponse('Inicio')

def compradores(request):
    
    fecha_actual = datetime.now()
    datos = {'fecha actual':fecha_actual}

    return render(request, 'base.html', datos)

