from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models

# Create your views here.


# def index(request) -> HttpResponse:
#     return redirect('/agenda/')


def login_user(request) -> HttpResponse:
    return render(request, 'login.html')


def logout_user(request) -> HttpResponse:
    logout(request)
    return redirect('/')


def submit_login(request) -> HttpResponse:
    # Se o tipo do request não for POST, retorna para a página anterior
    if not request.POST:
        return redirect('/')

    username = request.POST.get('username')
    password = request.POST.get('password')
    usuario = authenticate(username=username, password=password)
    if not usuario:
        messages.error(request, "Usuário ou senha inválido!")
        return redirect('/')

    login(request, usuario)
    return redirect('/')




def get_local(request, titulo_evento: str) -> HttpResponse:
    evento = models.Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)


@login_required(login_url="/login/")
def lista_eventos(request) -> HttpResponse:
    usuario = request.user
    eventos = models.Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)
