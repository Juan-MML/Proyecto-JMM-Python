from django.urls import path
from inicio.views import inicio,register,new_order,buscar_usuario,about

urlpatterns=[
    path('', inicio, name='inicio'),
    path('register/', register, name='register'),
    path('new-order/', new_order, name='new_order'),
    path('buscar-usuario/', buscar_usuario, name='buscar_usuario'),
    path('about/', about, name='about')
]