from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.forms import RegisterFormulario,BuscarCliente,EditarUsuario
from inicio.models import Cliente
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request,'index.html')

@login_required
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

@login_required
def new_order(request):
    return render(request,'new_order.html')

@login_required
def buscar_usuario(request):
    
    formulario = BuscarCliente(request.GET)
    if formulario.is_valid():
        cliente = formulario.cleaned_data.get('cliente')
        clientes = Cliente.objects.filter(cliente__icontains=cliente)
    
    return render(request,'buscar_usuario.html', {'clientes': clientes, 'form':formulario})

@login_required
def ver_usuario(request,id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'ver_usuario.html', {'cliente':cliente})

@login_required
def eliminar_usuario(request,id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('buscar_usuario')

@login_required
def editar_usuario(request,id):
    
    cliente = Cliente.objects.get(id=id)
    
    formulario = EditarUsuario(initial={'cliente':cliente.cliente, 'email':cliente.email, 'direccion':cliente.direccion, 'edad':cliente.edad, 'intereses':cliente.intereses})
    
    if request.method == "POST":
        formulario = EditarUsuario(request.POST)
        if formulario.is_valid():
            cliente.cliente = formulario.cleaned_data.get('cliente')
            cliente.email = formulario.cleaned_data.get('email')
            cliente.direccion = formulario.cleaned_data.get('direccion')
            cliente.edad = formulario.cleaned_data.get('edad')
            cliente.intereses = formulario.cleaned_data.get('intereses')
            
            cliente.save()
    
            return redirect('buscar_usuario')
    return render(request, 'editar_usuario.html', {'cliente':cliente, 'form': formulario})


def about(request):
    return render(request,'about.html')