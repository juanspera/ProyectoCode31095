import datetime

from django.shortcuts import render, redirect

from AppCoder.forms import CursoFormulario, BusquedaCamadaFormulario
from AppCoder.models import Curso, Entregable


def busqueda_camada_post(request):
    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    contexto = {
        'cursos': cursos
    }

    return render(request, 'AppCoder/curso_filtrado.html', contexto)


def busqueda_camada(request):

    contexto = {
        'form': BusquedaCamadaFormulario(),
    }

    return render(request, 'AppCoder/busqueda_camada.html', contexto)



def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso1.save()

            return redirect('AppCoderCursoFormulario')

    cursos = Curso.objects.all()

    contexto = {
        'form': CursoFormulario(),
        'cursos': cursos
    }

    return render(request, 'AppCoder/curso_formulario.html', contexto)


def inicio(request):
    contexto = {
        "valor1": "este es un valor"
    }
    return render(request, 'index.html', contexto)

def curso(request):
    curso1 = Curso(nombre="Python", camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1
    }

    return render(request, 'AppCoder/curso.html', contexto)

def entregable(request):
    entregables = [
        {
            'nombre': "",
            'fecha': "",
            'entregado': True
        },
        {
            'nombre': "",
            'fecha': "",
            'entregado': True
        },
        {
            'nombre': "",
            'fecha': "",
            'entregado': True
        },
    ]
    year = 2000
    month = 10
    day = 21
    entregable1 = Entregable(
        nombre="Luis",
        fecha_de_entrega=datetime.date(year=year, month=month, day=day),  # date year month day
        entregado=True
    )
    entregable1.save()

    contexto = {
        'entregable': entregable1
    }

    return render(request, 'AppCoder/entregable.html', contexto)
