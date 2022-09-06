from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserCoder.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'Porfavor verificar usuario o contrasenia!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('AppCoderInicio')

    contexto = {
        'form': AuthenticationForm(),
        'nombre_form': 'Login'
    }
    return render(request, 'UserCoder/login.html', contexto)


def register(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('AppCoderInicio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
    }

    return render(request, 'UserCoder/login.html', contexto)
