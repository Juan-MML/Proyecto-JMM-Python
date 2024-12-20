from django.db import models
from django.contrib.auth.models import User

class InformacionExtra(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares',blank=True,null=True)
    biography = models.CharField(max_length=500, blank=True)
