from django.db import models

class Productos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    descripcion = models.CharField(max_length=100, blank=True)
    creador = models.CharField(max_length=20)
    stock_arg = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)

    
    def __str__(self):
        return f'{self.id} {self.modelo} {self.descripcion}'
