from django.urls import path
from equipos.views import *

urlpatterns = [
    path('miequipo/<int:equipo_id>',mi_equipo,name='equipo-id')
]
