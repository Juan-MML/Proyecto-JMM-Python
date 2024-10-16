from django.db import models

class Cliente(models.Model):
    
        cliente = models.CharField(max_length=50)
        email = models.CharField(max_length=35)
        direccion = models.CharField(max_length=40)
        edad = models.IntegerField()
        intereses = models.CharField(max_length=200)
        
        def __str__(self):
                return f'{self.id} {self.cliente} {self.email} {self.direccion} {self.edad} {self.intereses}'
        