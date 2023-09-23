from django.shortcuts import render
import datetime
from .models import * 
from django.contrib.auth.models import User
from equipos.models import *
# Create your views here.



def home(request):


    campeonatos=Campeonato.objects.all().order_by('-fecha_inicio')

    
    dirigentes=Dirigentes.objects.all()

    return render(request,'home.html',{"campeonatos":campeonatos , "dirigentes":dirigentes})





def all_campeonatos(request):
    campeonatos=Campeonato.objects.all()
    dirigentes=Dirigentes.objects.all()
    return render(request,'campeonatos.html',{"campeonatos":campeonatos,"dirigentes":dirigentes})



def campeonato_id(request,campe_id):
    campeonato=Campeonato.objects.get(id=campe_id)
    dirigentes=Dirigentes.objects.all().filter(campeonato_asociado=campe_id)
    equipos=Equipo.objects.all().filter(campeonato=campe_id)
    jugadores=Jugadores.objects.all().filter(equipo__campeonato__id=campe_id)
    campeon=Equipo.objects.get(id=2)

    return render(request,'campeonato_id.html',{
        "campeonato":campeonato,
        "dirigentes":dirigentes,
        "equipos":equipos,
        "jugadores":jugadores,
        "campeon":campeon
        })