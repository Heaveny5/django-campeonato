from django.db import models
from django.contrib.auth.models import AbstractUser 
from campeonato.models import *
from equipos.models import *
from django.db.models import Model
# Create your models here.



class MensajeriaDirigente(Model):
    emisor=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    receptor=models.ForeignKey(Dirigentes, on_delete=models.CASCADE)
    asunto=models.CharField(max_length=150) 
    descripcion=models.CharField(max_length=300)
    archivo=models.FileField(upload_to='uploads/Documentos/%Y/%m/%d/',blank=True)