from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
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

