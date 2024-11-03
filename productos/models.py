from django.db import models

class Productos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    
    def __str__(self):
        return f'{self.id} {self.modelo}'