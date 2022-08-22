import datetime

from django.shortcuts import render

from AppCoder.models import Curso, Entregable


def curso(request):
    curso1 = Curso(nombre="Python", camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1
    }

    return render(request, 'curso.html', contexto)

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

    return render(request, 'entregable.html', contexto)
