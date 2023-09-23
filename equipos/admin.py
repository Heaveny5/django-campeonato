from django.contrib import admin
from equipos.models import *

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display=("Nombre" , "delegado","campeonato")
    search_fields=("Nombre","delegado","campeonato","delegado__first_name")
    list_filter=("Nombre","campeonato","delegado__first_name")


class JugadoreAdmin(admin.ModelAdmin):
    list_display=("Nombre" , "apellidos","fecha_nacimiento","estado","equipo")
    search_fields=("Nombre","apellidos","equipo","estado")
    list_filter=("estado","equipo__campeonato","equipo__Nombre")



class GruposAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    list_filter=("nombre","equipos")

admin.site.register(Jugadores,JugadoreAdmin) 
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Grupo,GruposAdmin)