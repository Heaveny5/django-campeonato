from django.urls import path
from usuario_login.views import *


urlpatterns = [
    path('login/',login_usuario,name='login'),
    path('logout/',logout_usuario,name="logout") 
]
