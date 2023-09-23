from django.db import models
from django.db.models import Model

# Create your models here.






class Campeonato(Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=500)
    lugar=models.CharField(max_length=500 , default="")
    fecha_inicio=models.DateField(verbose_name="Inicio Campeonato" )
    fecha_fin=models.DateField(verbose_name="Fin Campeonato")
    restriccion=models.CharField(verbose_name="Principal Restriccion" , max_length=500)
    


    def __str__(self) -> str:
        return "%s"%(self.nombre)
    

class Dirigentes(Model):
    nombre=models.CharField(max_length=200 , unique=True)
    apellido=models.CharField(max_length=100)
    cargo=models.CharField(max_length=200)
    campeonato_asociado=models.ManyToManyField(Campeonato)

    def __str__(self) -> str: 
        return "Apellido : %s - Nombre : %s - Cargo : %s "%(self.apellido,self.nombre,self.cargo)
    

