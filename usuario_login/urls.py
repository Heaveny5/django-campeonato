from django.urls import path
from usuario_login.views import *


urlpatterns = [
    path('login/',login_usuario,name='login'),
    path('logout/',logout_usuario,name="logout"),
    path('panel/<int:user_id>',panel_usuario,name='panel_user'),  
    path('panel/reclamo/<int:user_id>',form_reclamo, name="reclamo")
]
