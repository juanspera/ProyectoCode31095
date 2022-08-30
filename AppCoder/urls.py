from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', curso, name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderEntregable'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
]
