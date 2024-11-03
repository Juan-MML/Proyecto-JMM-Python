from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Productos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CrearProducto(CreateView):
    model = Productos
    template_name = "productos/crear_productos.html"
    success_url = reverse_lazy('productos:listado_productos')
    fields = ['marca','modelo','fecha_ingreso','descripcion','creador','stock_arg','imagen']
    
class ListadoProductos(ListView):
    model = Productos
    template_name = "productos/listado_productos.html"
    context_object_name = 'productos'

class VerProducto(DetailView):
    model = Productos
    template_name = "productos/ver_productos.html"
    context_object_name = 'productos'
    
class EditarProducto(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = "productos/editar_productos.html"
    success_url = reverse_lazy('productos:listado_productos')
    fields = ['marca','modelo','fecha_ingreso','descripcion','creador','stock_arg','imagen']
    
    def form_valid(self, form):
        form.instance.imagen = self.request.FILES.get('imagen', form.instance.imagen)
        return super().form_valid(form)

class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "productos/eliminar_productos.html"
    success_url = reverse_lazy('productos:listado_productos')

