from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Productos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CrearProducto(CreateView):
    model = Productos
    template_name = "productos/crear_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['marca','modelo','fecha_ingreso']
    
class ListadoPaletas(ListView):
    model = Productos
    template_name = "productos/listado_paletas.html"
    context_object_name = 'productos'

class VerPaleta(DetailView):
    model = Productos
    template_name = "productos/ver_paleta.html"
    
class EditarPaleta(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = "productos/editar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['marca','modelo','fecha_ingreso']

class EliminarPaleta(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "productos/eliminar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')

