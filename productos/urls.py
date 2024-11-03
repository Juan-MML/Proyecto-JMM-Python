from django.urls import path
from productos import views

app_name = 'productos'

urlpatterns = [
    path('productos/',views.ListadoPaletas.as_view(),name='listado_paletas'),
    path('productos/crear_paleta',views.CrearProducto.as_view(),name='crear_paleta'),
    path('productos/<int:pk>/',views.VerPaleta.as_view(),name='ver_paleta'),
    path('productos/<int:pk>/editar/',views.EditarPaleta.as_view(),name='editar_paleta'),
    path('productos/<int:pk>/eliminar/',views.EliminarPaleta.as_view(),name='eliminar_paleta')
]
