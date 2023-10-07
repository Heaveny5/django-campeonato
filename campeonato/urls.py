from django.urls import path
from campeonato.views import *

urlpatterns = [
    path('campeonatos/',all_campeonatos,name='campeonatos'),
    path('campeonatos/<int:campe_id>',campeonato_por_id,name="campeonato-id")
    
]
