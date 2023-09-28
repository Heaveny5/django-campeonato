from django.contrib import admin
from encuentros_equipos.models import *
# Register your models here.


class EncuentroAdmin(admin.ModelAdmin):
    list_display=("fecha","equipo_local","equipo_visitante","campeonato","fase")
    list_filter=("fecha","campeonato")
    

class SancionesAdmin(admin.ModelAdmin):
    list_filter=("equipo","jugador","fecha_inicio","fecha_fin")
    list_display=("equipo","jugador","fecha_inicio","fecha_fin","descripcion")


class ResultadoAdmin(admin.ModelAdmin):
    list_filter=("ganador","perdedor","empate")
    list_display=("encuentro","ganador","perdedor","empate")
    


admin.site.register(Encuentro,EncuentroAdmin)
admin.site.register(Sanciones,SancionesAdmin)
admin.site.register(Resultado,ResultadoAdmin)
