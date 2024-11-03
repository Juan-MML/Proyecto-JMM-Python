from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import CreacionUsuario, EdicionPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InformacionExtra


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            nombre_de_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')

            usuario = authenticate(username=nombre_de_usuario, password=contrasenia)
            
            django_login(request,usuario)
            objeto_creado, booleano_o_no = InformacionExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')
            
    return render (request, 'usuarios/login.html', {'form':formulario})

def register(request):
    
    formulario = CreacionUsuario()
    if request.method == 'POST':
        formulario = CreacionUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('usuarios:login')
    
    return render(request,'usuarios/register.html', {'form':formulario})

@login_required
def editar_perfil(request):
    
    informacion_extra = request.user.informacionextra
    formulario = EdicionPerfil(instance=request.user, initial={'avatar':informacion_extra.avatar})
    
    if request.method == "POST":
        
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            informacion_extra.avatar = nuevo_avatar if nuevo_avatar else informacion_extra.avatar
            
            informacion_extra.save()
            formulario.save()
            
            return redirect('inicio')

    return render(request, 'usuarios/editar_perfil.html', {'form':formulario})

class CambiarPassword(LoginRequiredMixin,PasswordChangeView):
    
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')
