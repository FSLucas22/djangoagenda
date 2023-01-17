from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from . import models

# Create your views here.


# def index(request) -> HttpResponse:
#     return redirect('/agenda/')


requires_login = login_required(login_url="/login/")


def login_user(request) -> HttpResponse:
    return render(request, 'login.html')


def logout_user(request) -> HttpResponse:
    logout(request)
    return redirect('/')


def submit_login(request) -> HttpResponse:
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


@requires_login
def lista_eventos(request) -> HttpResponse:
    usuario = request.user
    eventos = models.Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)


@requires_login
def evento(request) -> HttpResponse:
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        evento = models.Evento.objects.get(id=id_evento)
        if evento.usuario == request.user:
            dados['evento'] = models.Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)


@requires_login
def submit_evento(request) -> HttpResponse:
    if not request.POST:
        return redirect('/')

    evento_id = request.POST.get('id')
    titulo = request.POST.get('titulo')
    data_evento = request.POST.get('data')
    local_evento = request.POST.get('local')
    descricao = request.POST.get('descricao')
    usuario = request.user
    if not evento_id:
        models.Evento.objects.create(
            titulo=titulo,
            descricao=descricao,
            data_evento=data_evento,
            local=local_evento,
            usuario=usuario
        )
    else:
        evento = models.Evento.objects.get(id=evento_id)
        if evento.usuario != usuario:
            return redirect('/')
        evento.titulo = titulo
        evento.descricao = descricao,
        evento.data_evento = data_evento,
        evento.local = local_evento
        evento.save()
    return redirect('/')


@requires_login
def delete_evento(request, id_evento: int) -> HttpResponse:
    usuario = request.user
    try:
        evento = models.Evento.objects.get(id=id_evento)
        if evento.usuario == usuario:
            evento.delete()
    except ObjectDoesNotExist as e:
        pass
    return redirect('/')
