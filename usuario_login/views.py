from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from equipos.models import *
from campeonato.models import*
from usuario_login.models import MensajeriaDirigente
# Create your views here.



def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password'] 
        
        # Realiza la autenticación del usuario.
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si el usuario es válido, inicia sesión.
            login(request, user) 
            # Después de iniciar sesión, redirige a la página deseada.
            return redirect('home')
    
    # Si la solicitud no es un POST o la autenticación falla, renderiza el formulario personalizado.
    return render(request,'form_login.html')



def logout_usuario(request):
    logout(request)
    return redirect('home')


@login_required(login_url='home')
def panel_usuario(request,user_id):

    if request.user.is_superuser:
        return redirect("/admin")

    try:

        usuario=User.objects.get(pk=user_id)
        #print(usuario)
        is_delegado=usuario.groups.filter(name="Delegados").exists();
        
        equipo=Equipo.objects.get(delegado=user_id)
    
        #print(equipo)
        jugadores=Jugadores.objects.filter(equipo__id=equipo.id)
        print(equipo.logo)
        if is_delegado:
            pass
    except Exception:
        equipo=None
        jugadores=None
 


    return render(request,'panel_jugadores.html',{"equipo":equipo,"jugadores":jugadores})



@login_required(login_url='home')
def form_reclamo(request, user_id):
    
    id_equi=Equipo.objects.get(delegado=user_id)
    campeonato=Campeonato.objects.get(id=id_equi.campeonato.id)
    dirigentes=Dirigentes.objects.filter(campeonato_asociado=campeonato.id)

    #print(id_equi)
    
    if request.method=="POST":
        receptor_id=request.POST.get('receptor')
        asunto=request.POST['asunto']
        descripcion=request.POST['descripcion']
        archivo=request.FILES.get('archivo')


        receptor=Dirigentes.objects.get(id=receptor_id)
        emisor=Equipo.objects.get(delegado=user_id)

        print(receptor)
        print(emisor)
        print(asunto)
        print(descripcion)
        print(archivo)
        if asunto and descripcion and archivo:

            mensajeria=MensajeriaDirigente(
                emisor=emisor,
                receptor=receptor,
                asunto=asunto,
                descripcion=descripcion,
                archivo=archivo
            )

            mensajeria.save()

            return redirect('reclamo',user_id)


    return render(request,'panel_reclamo.html',{"equipo":id_equi ,"dirigentes":dirigentes})