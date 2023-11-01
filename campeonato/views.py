from django.shortcuts import render
import datetime
from .models import * 
from django.contrib.auth.models import User
from equipos.models import *
from encuentros_equipos.models import Encuentro
# Create your views here.



def home(request):


    campeonatos=Campeonato.objects.all().order_by('-fecha_inicio')

    
    dirigentes=Dirigentes.objects.all()

    return render(request,'home.html',{"campeonatos":campeonatos , "dirigentes":dirigentes})





def all_campeonatos(request):
    campeonatos=Campeonato.objects.all()
    dirigentes=Dirigentes.objects.all()
    return render(request,'campeonatos.html',{"campeonatos":campeonatos,"dirigentes":dirigentes})



def campeonato_por_id(request,campe_id):
    campeonato=Campeonato.objects.get(id=campe_id)
    dirigentes=Dirigentes.objects.all().filter(campeonato_asociado=campe_id)
    equipos=Equipo.objects.all().filter(campeonato=campe_id)
    jugadores=Jugadores.objects.all().filter(equipo__campeonato__id=campe_id)
    campeon=Equipo.objects.get(id=2)
    encuentros=Encuentro.objects.all().filter(campeonato_id=campeonato)
    grupos=Grupo.objects.all()
    #error
    

    


    for grupo in grupos:
        for encuentro in encuentros:
            if grupo.id:
                print(encuentro.equipo_local ,encuentro.equipo_visitante)
                print(encuentro.goles_local)

    #print(resultados)
    return render(request,'campeonato_id.html',{
        "campeonato":campeonato,
        "dirigentes":dirigentes,
        "equipos":equipos,
        "jugadores":jugadores,
        "campeon":campeon,
        "encuentros":encuentros,
        "grupos":grupos
        })





#esto es para los vs de equipos 


        # <div>
        #     <div class="partido">
        #         <div class="equipo">Equipo A1</div>
        #         <div class="vs">vs</div>
        #         <div class="equipo">Equipo B2</div>
        #     </div>
        
        #     <div class="partido">
        #         <div class="equipo">Equipo C1</div>
        #         <div class="vs">vs</div>
        #         <div class="equipo">Equipo D2</div>
        #     </div>
        
        #     <div class="partido">
        #         <div class="equipo">Equipo E1</div>
        #         <div class="vs">vs</div>
        #         <div class="equipo">Equipo F2</div>
        #     </div>
        # </div>
#         .partido {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     margin-bottom: 20px;
# }
# .equipo {
#     padding: 10px;
#     border: 1px solid #ccc;
#     margin: 0 10px;
# }
# .vs {
#     font-size: 24px;
#     margin: 0 20px;
# }