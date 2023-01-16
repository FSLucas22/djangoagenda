from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def get_local(request, titulo_evento: str) -> HttpResponse:
    evento = models.Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)
