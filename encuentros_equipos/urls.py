from django.urls import path
from encuentros_equipos.views import mis_resultados,añadir_jugador,setings_usuario,actualizar_jugador



urlpatterns = [ 
    path('panel/resultados/<int:user_id>',mis_resultados, name="resultado"),
    path("panel/añadir_jugador/<int:user_id>",añadir_jugador , name="añadir_jugador"),
    path("panel/settings/perfil/<int:user_id>",setings_usuario , name="settings"),
    path("panel/actualizar_jugador/<int:user_id>/<int:jugador_id>", actualizar_jugador ,name='actualizar_jugador')
]
 