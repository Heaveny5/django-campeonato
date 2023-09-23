from django.contrib import admin
from campeonato.models import *
# Register your models here.

class CampeonatoAdmin(admin.ModelAdmin):
    list_display=("nombre","fecha_inicio","fecha_fin","restriccion","lugar")
    search_fields=("nombre","fecha_inicio","fecha_fin","lugar")
    list_filter=("id","fecha_inicio","fecha_fin")
    fieldsets=(
        ("Nombre", {
            "fields": ("nombre",),
            "description": "Note: ingrese el nombre del campeonato  ",
        }),
        ("Tipo", {
            "fields": ("tipo",),
            "description": "Note: Ejemplo( verano , invierno ) ",
        }),
        ("Lugar ", {
            "fields": ("lugar",),
            "description": "Note: Ingrese lugar donde se realizara el campeonato",
        }),
        ("Fecha Inicio", {
            "fields": ("fecha_inicio",),
            "description": "Note: ingrese una fecha valida que no coincida con otra ",
        }),
        ("Fecha Fin ", {
            "fields": ("fecha_fin",),
            "description": "Note: Ingrese fecha valida y posterior al inicio  ",
        }),
        ("Restricion Principal - Bases ", {
            "fields": ("restriccion",),
            "description": "Note: Ejemplo (master en equipo , sub17 en equipo) ",
        }),
    )

class DirigentesAdmin(admin.ModelAdmin):
    list_display=("nombre" , "apellido","cargo",)
    search_fields=("nombre","apellido","cargo",)
    list_filter=("cargo","campeonato_asociado")



admin.site.register(Campeonato,CampeonatoAdmin) 
admin.site.register(Dirigentes,DirigentesAdmin)