from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('registro/', view=views.registro, name='registro'),
    path('logout/', view=views.cerrar_sesion, name='logout'),
    path('login/', view=views.iniciar_sesion, name='login'),
]
