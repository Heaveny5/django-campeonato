from django.urls import path
from encuentros_equipos.views import mis_resultados



urlpatterns = [ 
    path('panel/resultados/<int:user_id>',mis_resultados, name="resultado")
]
