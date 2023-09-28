from django.shortcuts import render,redirect
from encuentros_equipos.models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from equipos.models import *
from campeonato.models import*
from django.db.models import Q


@login_required(login_url='home')
def mis_resultados(request,user_id):

    try:
        equipo=Equipo.objects.get(delegado=user_id)
        campeonato=Campeonato.objects.get(equipo=equipo)
        encuentro=Encuentro.objects.filter(Q(equipo_local=equipo)|Q(equipo_visitante=equipo))
        resultado=Resultado.objects.filter(encuentro__in=encuentro)


        #print(equipo)
        #print(campeonato)
        #print(encuentro)
        for encuent in encuentro:
            for result in resultado:
                if encuent.id==result.encuentro.id:
                    print(result)
        #print(resultado)
    except Exception:
        return redirect('home')

    return render(request,'panel_encuentros.html',{"equipo":equipo ,
                                                   "campeonato":campeonato,
                                                   "encuentros":encuentro,
                                                   "resultados":resultado
                                                   })

