from django.urls import path

from AppCoder.views import curso, entregable, inicio

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', curso, name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderEntregable')
]
