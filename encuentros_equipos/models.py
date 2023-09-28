from django.db import models
from django.db.models import Model
from equipos.models import *
# Create your models here.



class Encuentro(Model):
    fecha=models.DateField()
    hora_inicio=models.CharField(verbose_name="Hora Inicio",max_length=5)
    hora_fin=models.CharField(verbose_name="Hora Fin",max_length=5)
    equipo_local=models.ForeignKey(Equipo,verbose_name="Local",on_delete=models.CASCADE,related_name="Local")
    equipo_visitante=models.ForeignKey(Equipo,verbose_name="Visitante",on_delete=models.CASCADE,related_name="Visitante")
    campeonato=models.ForeignKey(Campeonato,on_delete=models.CASCADE,verbose_name="Campeonato")
    fase=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return "Equipo 1: %s - Equipo 2: %s"%(self.equipo_local,self.equipo_visitante)


class Sanciones(Model):
    fecha_inicio=models.DateField(verbose_name="Fecha Inicio") 
    fecha_fin=models.DateField(verbose_name="Fecha Fin")
    equipo=models.ForeignKey(Equipo,null=True,blank=True,on_delete=models.CASCADE)
    jugador=models.ForeignKey(Jugadores,null=True,blank=True, on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=100)

    def __str__(self) -> str:
        return "jugador: %s - Equipo: %s "%(self.jugador.Nombre,self.equipo.Nombre)


class Resultado(Model):
    ganador=models.ForeignKey(Equipo,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Ganador",related_name="Ganador")
    perdedor=models.ForeignKey(Equipo,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Perdedor",related_name="Perdedor")
    empate=models.BooleanField(default=False)
    encuentro=models.ForeignKey(Encuentro,on_delete=models.CASCADE)
    goles_ganador=models.IntegerField(default=0)
    goles_perdedor=models.IntegerField(default=0)
    def __str__(self):
        return "Ganador: %s - Perdedor %s"%(self.ganador,self.perdedor)
    





