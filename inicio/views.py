from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.forms import RegisterFormulario,BuscarCliente
from inicio.models import Cliente


def inicio(request):
    return render(request,'index.html')

def register(request):
    
    #print('Request', request)
    #print('GET', request.GET)
    #print('POST', request.POST)
    
    formulario = RegisterFormulario()
    
    if request.method == 'POST':
        
        formulario = RegisterFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Cliente(cliente=data.get('cliente'),email=data.get('email'), direccion=data.get('direccion'), edad=data.get('edad'),intereses=data.get('intereses'))
            cliente.save()
            return redirect('buscar_usuario')

    return render(request, 'register.html', {'form':formulario})

def new_order(request):
    return render(request,'new_order.html')

def buscar_usuario(request):
    
    formulario = BuscarCliente(request.GET)
    if formulario.is_valid():
        cliente = formulario.cleaned_data.get('cliente')
        clientes = Cliente.objects.filter(cliente__icontains=cliente)
    
    return render(request,'buscar_usuario.html', {'clientes': clientes, 'form':formulario})

def about(request):
    return render(request,'about.html')