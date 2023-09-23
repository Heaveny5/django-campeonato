from django.shortcuts import render
from django.contrib.auth.models import User
from equipos.models import *
from datetime import date

from django.db.models import ExpressionWrapper
from django.db.models.functions import Now
# Create your views here.


 #usuario=User.objects.create_user(username="asd",password='asd',first_name=)




def all_equipos(request):

    equipos=Equipo.objects.all()
    campeonato=Campeonato.objects.all()

    return render(request,'equipos.html',{"equipos":equipos,"campeonato":campeonato})




def mi_equipo(request,equipo_id):

    equipo=Equipo.objects.get(id=equipo_id)
    jugadores=Jugadores.objects.all().filter(equipo__id=equipo_id)
    fecha_actual=date.today()
    fecha=fecha_actual.year
    edad_jugadores={}
    for jugador in jugadores:
        print(jugador.fecha_nacimiento.year)
        print(fecha)
        a=abs(jugador.fecha_nacimiento.year-fecha)
        edad_jugadores[jugador.id]=a 

    #print(edad_jugadores)
    return render(request,'equipo_id.html',{
        "equipo":equipo,
        "jugadores":jugadores,
        "edad_jugadores":edad_jugadores
        })

