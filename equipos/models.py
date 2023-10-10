from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from campeonato.models import Campeonato,Dirigentes
# Create your models here.

class Equipo(Model):
    Nombre=models.CharField(max_length=100,unique=True)
    delegado=models.ForeignKey(User,on_delete=models.CASCADE)
    foto_equipo=models.ImageField(upload_to='equipos' , null=True , blank=True)
    logo=models.ImageField(upload_to='logo_equipos', default='media/default.png')
    campeonato=models.ForeignKey(Campeonato , on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "%s - Delegado: %s"%(self.Nombre,self.delegado.first_name)




class Jugadores(Model):
    Nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    estado=models.BooleanField(default=True)
    imagen_dni=models.ImageField(upload_to='jugadores' , default='media/default.png')
    equipo=models.ForeignKey(Equipo,on_delete=models.CASCADE)
    goles_max=models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return "Nombre: %s - Equipo: %s"%(self.Nombre,self.equipo.Nombre)



class Grupo(Model):
    nombre=models.CharField(max_length=1 , verbose_name="Grupo", default="-")
    equipos=models.ManyToManyField(Equipo , related_name="grupo")


    


    def __str__(self) -> str:
        return "Grupo: %s"%(self.nombre)





