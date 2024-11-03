from django.urls import path
from productos import views

app_name = 'productos'

urlpatterns = [
    path('productos/',views.ListadoProductos.as_view(),name='listado_productos'),
    path('productos/crear_producto',views.CrearProducto.as_view(),name='crear_producto'),
    path('productos/<int:pk>/',views.VerProducto.as_view(),name='ver_producto'),
    path('productos/<int:pk>/editar/',views.EditarProducto.as_view(),name='editar_producto'),
    path('productos/<int:pk>/eliminar/',views.EliminarProducto.as_view(),name='eliminar_producto')
]
