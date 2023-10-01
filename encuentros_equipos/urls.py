from django.urls import path
from encuentros_equipos.views import mis_resultados,añadir_jugador



urlpatterns = [ 
    path('panel/resultados/<int:user_id>',mis_resultados, name="resultado"),
    path("panel/añadir_jugador/<int:user_id>",añadir_jugador , name="añadir_jugador")
]
 