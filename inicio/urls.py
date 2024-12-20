from django.urls import path
from inicio.views import (inicio,
    buscar_usuario,
    ver_usuario,
    eliminar_usuario,
    editar_usuario,
    about)

urlpatterns=[
    path('', inicio, name='inicio'),
    path('buscar-usuario/', buscar_usuario, name='buscar_usuario'),
    path('ver-usuario/<int:id>/', ver_usuario, name='ver_usuario'),
    path('eliminar-usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('editar-usuario/<int:id>/', editar_usuario, name='editar_usuario'),
    path('about/', about, name='about')
]