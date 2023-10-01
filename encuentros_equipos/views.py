from django.shortcuts import render,redirect
from encuentros_equipos.models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from equipos.models import *
from campeonato.models import*
from django.db.models import Q
from django.urls import reverse
import datetime

@login_required(login_url='login')
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




@login_required(login_url='login')
def añadir_jugador(request,user_id):

    try:
        equipo=Equipo.objects.get(delegado=user_id)
        usuario=equipo.delegado.id
        url=reverse('panel_user',args=[usuario])
        print(usuario)
        print(equipo)
        if request.method=="POST":
            nombre=request.POST["nombre"]
            apellidos=request.POST["apellidos"]
            fecha_nacimiento=request.POST.get("fecha_nacimiento",datetime.datetime.now().date())
            imagen_dni=request.FILES.get("imagen_dni")

            print(nombre)
            print(apellidos)
            print(fecha_nacimiento)
            print(imagen_dni)

            nuevo_jugador=Jugadores(
                Nombre=nombre,
                apellidos=apellidos,
                imagen_dni=imagen_dni,
                fecha_nacimiento=fecha_nacimiento,
                equipo=equipo
            )

            nuevo_jugador.save()

            return redirect(url)


    except Exception as e:
        print(e)
        return redirect('home')



    return render(request,'panel_añadir_jugador.html',{"equipo":equipo})
