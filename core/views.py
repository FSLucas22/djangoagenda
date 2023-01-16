from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.


# def index(request) -> HttpResponse:
#     return redirect('/agenda/')


def get_local(request, titulo_evento: str) -> HttpResponse:
    evento = models.Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)


def lista_eventos(request) -> HttpResponse:
    # usuario = request.user
    # eventos = models.Evento.objects.filter(usuario=usuario)
    eventos = models.Evento.objects.all()
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)
