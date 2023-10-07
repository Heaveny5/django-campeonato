from django.shortcuts import render,redirect
from encuentros_equipos.models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from equipos.models import *
from campeonato.models import*
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
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
        url=reverse('añadir_jugador',args=[usuario])
        print(usuario)
        print(equipo)
        if request.method=="POST":
            nombre=request.POST["nombre"]
            apellidos=request.POST["apellidos"]
            fecha_nacimiento=request.POST.get("fecha_nacimiento",datetime.datetime.now().date())
            imagen_dni=request.FILES.get("imagen_dni")

            # print(nombre)
            # print(apellidos)
            # print(fecha_nacimiento)
            # print(imagen_dni)
            usuario_user=User.objects.get(pk=user_id)
            cantidad_jugadores=Jugadores.objects.filter(equipo=equipo).count()
            if cantidad_jugadores>=11:
                messages.error(request,f"Se han alcanzado el limite de jugadores ({cantidad_jugadores})")
            else:
                print(usuario_user)
                nuevo_jugador=Jugadores(
                    Nombre=nombre,
                    apellidos=apellidos,
                    imagen_dni=imagen_dni,
                    fecha_nacimiento=fecha_nacimiento,
                    equipo=equipo
                )
                nuevo_jugador.save()
                messages.success(request,f"Jugador {nombre} añadido correctamente" )

    except Exception as e:
        print(e)
        return redirect('home')



    return render(request,'panel_añadir_jugador.html',{"equipo":equipo})






@login_required(login_url='login')
def setings_usuario(request,user_id):

    usuario=User.objects.get(pk=user_id)
    
    equipo=Equipo.objects.get(delegado=usuario)
    
    url=reverse('panel_user',args=[usuario.id])

    if request.method=="POST":

        #actualizar usuario
        nombre=request.POST['nombre_usuario']
        email=request.POST['correo_usuario']
        username=request.POST['username']

        #actualizar equipo
        imagen_equipo=request.FILES.get("imagen_equipo_settings")
        nombre_equipo=request.POST['nombre_equipo']

        if nombre:
            usuario.first_name=nombre
            messages.success(request,f"Nombre Actualizado Correctamente" )

        if email:
            usuario.email=email
            messages.success(request,f"Email Actualizado Correctamente" )
        if username:
            usuario.username=username
            messages.success(request,f"Username Actualizado correctamente" )
        if imagen_equipo:
            equipo.logo=imagen_equipo
            messages.success(request,f"Logo Equipo Actualizado correctamente" )
        if nombre_equipo:
            equipo.Nombre=nombre_equipo
            messages.success(request,f"Nombre Equipo Actualizado correctamente" )

        usuario.save()
    
        

    return render(request,'panel_settings.html',{"usuario":usuario,"equipo":equipo})





@login_required(login_url='login')
def actualizar_jugador(request,user_id,jugador_id):

    usuario=User.objects.get(pk=user_id)
    equipo=Equipo.objects.get(delegado=usuario)
    jugador=Jugadores.objects.get(pk=jugador_id)
    url=reverse('panel_user',args=[usuario.id])

    print(user_id,jugador_id)
    if request.method=="POST":
        nombre=request.POST["nombre_jugador_panel"]
        apellido=request.POST["apellido_jugador_panel"]
        fecha_nacimiento=request.POST.get("fecha_nacimiento",datetime.datetime.now().date())
        dni_img=request.FILES.get("imagen_equipo_settings")
        accion=request.POST.get("accion")
        

        if accion=="eliminar":
            jugador.delete()
            return redirect(url)

        elif accion=="guardar_cambios":
            if nombre:
                jugador.Nombre=nombre
                messages.success(request,f"Nombre Actualizado Correctamente" )
            if apellido:
                jugador.apellidos=apellido
                messages.success(request,f"Apellido Actualizado Correctamente" )
            if fecha_nacimiento:
                jugador.fecha_nacimiento=fecha_nacimiento
                messages.success(request,f"Fecha Nacimiento Actualizado correctamente" )
            if dni_img:
                jugador.imagen_dni=dni_img
                messages.success(request,f"Imagen DNI Equipo Actualizado correctamente" )
            
            jugador.save()


    return render(request,'actualizar_jugador.html',{"usuario":usuario,"equipo":equipo,"jugador":jugador})