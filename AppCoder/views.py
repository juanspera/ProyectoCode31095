from django.shortcuts import render

from AppCoder.models import Curso


def curso(request):
    curso1 = Curso(nombre="Python", camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1
    }

    return render(request, 'curso.html', contexto)
