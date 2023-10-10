from django.contrib import admin
from encuentros_equipos.models import *
from django.contrib.admin import SimpleListFilter
# Register your models here.




class EncuentroAdmin(admin.ModelAdmin):
    list_display=("campeonato","equipo_local","equipo_visitante","fase")
    #list_filter=("fecha","campeonato") 

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'equipo_local' or db_field.name == 'equipo_visitante':
    #         # Filtra los equipos según el grupo seleccionado
    #         grupo_id = request.GET.get('grupo')
    #         print(grupo_id)
    #         if grupo_id:
    #             kwargs['queryset'] = Equipo.objects.filter(grupo_id=grupo_id)
    #         else:
    #             kwargs['queryset'] = Equipo.objects.none()  # Si no se ha seleccionado un grupo, muestra un queryset vacío
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)





class SancionesAdmin(admin.ModelAdmin):
    list_filter=("equipo","jugador","fecha_inicio","fecha_fin")
    list_display=("equipo","jugador","fecha_inicio","fecha_fin","descripcion")





admin.site.register(Encuentro,EncuentroAdmin)
admin.site.register(Sanciones,SancionesAdmin)

